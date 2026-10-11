import os
import asyncio
import logging
from datetime import datetime, timedelta
import pytz

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.exceptions import TelegramNetworkError
from dotenv import load_dotenv

import database as db

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
TASHKENT_TZ = pytz.timezone("Asia/Tashkent")

dp = Dispatcher(storage=MemoryStorage())

# Reja qo'shish holatlari (FSM)
class PlanState(StatesGroup):
    waiting_for_text = State()
    waiting_for_time = State()

# Asosiy menyu
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Yangi reja qo'shish")],
        [KeyboardButton(text="🗓 Mening rejalarim"), KeyboardButton(text="⚙️ Sozlamalar")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Kerakli bo'limni tanlang..."
)

cancel_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="❌ Bekor qilish")]],
    resize_keyboard=True
)

@dp.message(F.text == "❌ Bekor qilish")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Amal bekor qilindi.", reply_markup=main_menu)

@dp.message(CommandStart())
async def command_start_handler(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    try:
        await db.add_or_update_user(message.from_user.id, message.from_user.full_name)
    except Exception as e:
        logging.error(f"Foydalanuvchini bazaga yozishda xatolik: {e}")
    
    text = (
        f"Assalomu alaykum, {message.from_user.full_name}! 🥷\n\n"
        f"Sizni **TIME NINJA** botida ko'rib turganimizdan xursandmiz!\n"
        f"Barcha rejalaringiz xavfsiz tarzda **Supabase Cloud bazasida** saqlanadi.\n\n"
        f"Quyidagi menyudan kerakli bo'limni tanlang:"
    )
    await message.answer(text, reply_markup=main_menu, parse_mode="Markdown")

@dp.message(F.text == "📝 Yangi reja qo'shish")
async def add_plan_start(message: types.Message, state: FSMContext):
    await state.set_state(PlanState.waiting_for_text)
    await message.answer(
        "Qanday vazifani rejalashtirmoqchisiz?\n"
        "(Masalan: *Kitob o'qish*, *Ingliz tili darsi*, *Uchrashuv*):",
        reply_markup=cancel_menu,
        parse_mode="Markdown"
    )

@dp.message(PlanState.waiting_for_text)
async def process_plan_text(message: types.Message, state: FSMContext):
    await state.update_data(task_text=message.text)
    await state.set_state(PlanState.waiting_for_time)
    
    now = datetime.now(TASHKENT_TZ)
    example_time = (now + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
    
    await message.answer(
        "Vazifani qachon eslatay?\n\n"
        "Quyidagi formatlardan birida kiriting:\n"
        f"1. Aniq vaqt: `{example_time}` (Yil-Oy-Kun Soat:Daqiqa)\n"
        "2. Nisbiy vaqt: `10 daqiqa` yoki `2 soat`\n"
        "3. Bugun/Ertaga: `bugun 18:00` yoki `ertaga 09:30`",
        reply_markup=cancel_menu,
        parse_mode="Markdown"
    )

def parse_user_time(text: str) -> datetime | None:
    now = datetime.now(TASHKENT_TZ)
    text = text.strip().lower()
    
    if "daqiqa" in text or "min" in text:
        try:
            minutes = int(''.join(filter(str.isdigit, text)))
            return now + timedelta(minutes=minutes)
        except:
            pass

    if "soat" in text or "hour" in text:
        try:
            hours = int(''.join(filter(str.isdigit, text)))
            return now + timedelta(hours=hours)
        except:
            pass

    if text.startswith("bugun "):
        try:
            time_part = text.replace("bugun ", "").strip()
            target_time = datetime.strptime(time_part, "%H:%M").time()
            return now.replace(hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0)
        except:
            pass
            
    if text.startswith("ertaga "):
        try:
            time_part = text.replace("ertaga ", "").strip()
            target_time = datetime.strptime(time_part, "%H:%M").time()
            tomorrow = now + timedelta(days=1)
            return tomorrow.replace(hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0)
        except:
            pass

    for fmt in ("%Y-%m-%d %H:%M", "%d.%m.%Y %H:%M"):
        try:
            parsed = datetime.strptime(text, fmt)
            return TASHKENT_TZ.localize(parsed)
        except:
            pass
            
    return None

@dp.message(PlanState.waiting_for_time)
async def process_plan_time(message: types.Message, state: FSMContext):
    target_dt = parse_user_time(message.text)
    if not target_dt:
        await message.answer(
            "Vaqt formati tushunarsiz bo'ldi. Iltimos qaytadan kiriting:\n"
            "Masalan: `2026-10-12 15:30` yoki `15 daqiqa` yoki `ertaga 10:00`",
            parse_mode="Markdown"
        )
        return

    data = await state.get_data()
    task_text = data["task_text"]
    
    naive_dt = target_dt.replace(tzinfo=None)
    try:
        await db.add_plan(message.from_user.id, task_text, naive_dt)
    except Exception as e:
        logging.error(f"Rejani bazaga qo'shishda xatolik: {e}")
        await message.answer("Baza bilan vaqtinchalik xatolik yuz berdi. Iltimos qayta urinib ko'ring.")
        return

    await state.clear()
    formatted_time = target_dt.strftime("%Y-%m-%d %H:%M")
    await message.answer(
        f"Rejangiz muvaffaqiyatli saqlandi! 🎯\n\n"
        f"📌 **Vazifa:** {task_text}\n"
        f"⏰ **Eslatish vaqti:** {formatted_time}\n\n"
        f"Vaqti kelganda TIME NINJA sizga albatta xabar yuboradi!",
        reply_markup=main_menu,
        parse_mode="Markdown"
    )

@dp.message(F.text == "🗓 Mening rejalarim")
async def my_plans(message: types.Message):
    try:
        plans = await db.get_user_plans(message.from_user.id)
    except Exception as e:
        logging.error(f"Rejalarni olishda xatolik: {e}")
        await message.answer("Rejalarni yuklashda xatolik yuz berdi.")
        return

    if not plans:
        await message.answer(
            "Hozircha faol rejalaringiz yo'q. Yangi reja qo'shish uchun pastdagi tugmani bosing! 🥷",
            reply_markup=main_menu
        )
        return
        
    text = "🗓 **Sizning faol rejalaringiz:**\n\n"
    for i, plan in enumerate(plans, 1):
        p_time = plan["task_time"].strftime("%Y-%m-%d %H:%M")
        text += f"{i}. 📌 **{plan['task_text']}**\n   ⏰ Vaqti: `{p_time}`\n\n"
        
    await message.answer(text, reply_markup=main_menu, parse_mode="Markdown")

@dp.message(F.text == "⚙️ Sozlamalar")
async def settings_menu(message: types.Message):
    await message.answer("Sozlamalar bo'limi:\nVaqt mintaqasi: Asia/Tashkent (GMT+5)\nBaza holati: Supabase Connected ✅")

# Avtomatik eslatma yuboruvchi fon vazifasi
async def reminder_worker(bot: Bot):
    while True:
        try:
            due_plans = await db.get_due_plans()
            for plan in due_plans:
                try:
                    await bot.send_message(
                        chat_id=plan["user_id"],
                        text=(
                            f"🔔 **ESLATMA VAQTI KELDI!** 🥷\n\n"
                            f"📌 **Vazifangiz:** {plan['task_text']}\n"
                            f"Rejangizni o'z vaqtida bajaring!"
                        ),
                        parse_mode="Markdown"
                    )
                    await db.mark_plan_completed(plan["id"])
                except Exception as e:
                    logging.error(f"Xabar yuborishda xatolik: {e}")
        except Exception as e:
            logging.error(f"Workerda xatolik: {e}")
            
        await asyncio.sleep(20)

async def main() -> None:
    session = AiohttpSession(timeout=30.0)
    bot = Bot(token=BOT_TOKEN, session=session)
    asyncio.create_task(reminder_worker(bot))
    
    # Tarmoq uzilsa qayta ulanish mexanizmi (Auto-reconnect loop)
    while True:
        try:
            await dp.start_polling(bot, handle_signals=False)
        except TelegramNetworkError as e:
            logging.warning(f"Telegram tarmog'ida vaqtinchalik uzilish ({e}). 5 soniyadan so'ng qayta ulaniladi...")
            await asyncio.sleep(5)
        except Exception as e:
            logging.error(f"Kutilmagan xatolik: {e}. Qayta ishga tushirilmoqda...")
            await asyncio.sleep(5)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")
