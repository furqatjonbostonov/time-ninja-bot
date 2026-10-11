# TEXNIK TOPSHIRIQ (TZ): TELEGRAM VAZIFALAR VA ESLATMALAR TIZIMI (BOT + MINI APP)

**Hujjat kodi:** TZ-CENTRAL-ASIA-TASK-BOT-2026  
**Loyiha nomi:** Telegram Task & Reminder Bot + Telegram Mini App (TMA)  
**Mintaqaviy qamrov:** O'rta Osiyo (O'zbekiston, Qozog'iston, Qirg'iziston, Tojikiston, Turkmaniston)  
**Holati:** Tasdiqlangan / Ishlab chiqarishga tayyor (Production-Ready)  
**Versiya:** 1.0.0  
**Sana:** 2026-10-09  

---

## MUNDARIJA
1. [Loyihaning Umumiy Tavsifi va Maqsadi](#1-loyihaning-umumiy-tavsifi-va-maqsadi)
   - 1.1. Loyihaning Qisqacha Tavsifi (Executive Summary)
   - 1.2. Maqsadli Auditoriya va Foydalanuvchi Personalari
   - 1.3. Biznes Maqsadlari va Ko'rsatkichlar (KPIs)
   - 1.4. Texnik Maqsadlar va Arxitektura Prinsiplari
2. [Telegram Bot Xabarlar Mantig'i va Buyruqlar Tizimi](#2-telegram-bot-xabarlar-mantigi-va-buyruqlar-tizimi)
   - 2.1. Bot Buyruqlari Arxitekturasi va Standart Menyu
   - 2.2. Buyruqlarning Batafsil Ishlash Ssenariylari
   - 2.3. Deep Linking Mantig'i
   - 2.4. Fallback Chat FSM Mode (Suhbat Asosidagi Matnli Rejim)
   - 2.5. Quick Add NLP Regex Tahlilchisi
3. [Telegram Mini App (TMA) Sahifalari va UI/UX Interfeysi](#3-telegram-mini-app-tma-sahifalari-va-uiux-interfeysi)
   - 3.1. Telegram WebApp Native SDK Integratsiyasi
   - 3.2. TMA 6 Asosiy Sahifasining Batafsil Tuzilishi
4. [Vazifalar Hayot Sikli va Ma'lumotlar Modeli](#4-vazifalar-hayot-sikli-va-malumotlar-modeli)
   - 4.1. Vazifa Holatlari Mashinasi (5-State FSM)
   - 4.2. RFC 5545 RRULE Takrorlanish Dvigateli
   - 4.3. Relyatsion PostgreSQL DDL Sxemasi
5. [Vazifani Ogohlantirish (Notification) Jarayoni va Bosqichlari](#5-vazifani-ogohlantirish-notification-jarayoni-va-bosqichlari)
   - 5.1. 5 Bosqichli Ogohlantirish Quvuri (Multi-Stage Pipeline)
   - 5.2. Interaktiv Inline Tugmalar va Xabar Shabloni
   - 5.3. Tungi Tinchlik Rejimi (Quiet Hours / DND)
   - 5.4. Telegram Tezlik Cheklovlari (Rate Limits) va Xatoliklarni Boshqarish
6. [Vaqt Mintaqalari (Timezone) Boshqaruvi](#6-vaqt-mintaqalari-timezone-boshqaruvi)
   - 6.1. O'rta Osiyo Davlatlari va Vaqt Zonalari Xaritasi
   - 6.2. Vaqtni Saqlash va Konvertatsiya Qilish Matematikasi
7. [Nofunksional Talablar (NFRs)](#7-nofunksional-talablar-nfrs)
   - 7.1. Tezlik va Kechikish Ko'rsatkichlari (Performance & Latency)
   - 7.2. Ishonchlilik, Xavfsizlik va Barqarorlik (Reliability & Security)
   - 7.3. 4 Tilli Mahalliylashtirish (Localization & i18n)

---

## 1. Loyihaning Umumiy Tavsifi va Maqsadi

### 1.1. Loyihaning Qisqacha Tavsifi (Executive Summary)
Ushbu loyiha O'rta Osiyo mintaqasi foydalanuvchilari uchun maxsus moslashtirilgan, Telegram ekotizimi ichida to'liq ishlaydigan zamonaviy "Vazifalar va Eslatmalar" tizimidir. Tizim ikki asosiy poydevordan iborat:
1. **Telegram Bot:** Tezkor buyruqlar, tabiiy tildagi matnni (NLP) avtomatik parslash, interaktiv inline tugmalar orqali eslatmalarni surish/bajarish hamda internet sekin hududlar uchun suhbat asosidagi to'liq FSM (Finite State Machine) boshqaruvi.
2. **Telegram Mini App (TMA):** WebApp texnologiyasi asosida qurilgan, mobil ilovalar bilan tenglashadigan, taqvim, soatlik timeline, toifalar va analitik ko'rsatkichlarni o'z ichiga olgan boy grafik interfeys.

Loyiha O'rta Osiyoda Telegram messenjerining o'ta yuqori ommalashganligini (O'zbekistonda aholining 80%+ qismi Telegram'dan kundalik muloqot va biznesda foydalanadi) inobatga olgan holda, alohida og'ir mobil ilova o'rnatmasdan, bevosita messenjerning o'zida shaxsiy va jamoaviy mahsuldorlikni oshirishga xizmat qiladi.

### 1.2. Maqsadli Auditoriya va Foydalanuvchi Personalari
O'rta Osiyo bozorining ijtimoiy-iqtisodiy xususiyatlaridan kelib chiqib, 4 ta asosiy foydalanuvchi personasi shakllantirilgan:

1. **Persona 1: Alisher (24 yosh, Toshkent, O'zbekiston) — IT Mutaxassis / Frilanser**
   - *Foydalanish holati:* Kuniga 10-15 ta mijozlar topshirig'i, loyiha muddatlari, uchrashuvlar. Asosiy aloqa vositasi — Telegram.
   - *Ehtiyoji:* Vazifalarni tezkor belgilash, 15 daqiqa oldin eslatma olish, loyihalarni teglar (`#ish`, `#dasturlash`, `#shaxsiy`) bo'yicha ajratish.
   - *Qurilma & Tarmoq:* iPhone 14, 4G/Wi-Fi, doimiy onlayn rejim. Mini App'ning to'liq interfeysidan faol foydalanadi.

2. **Persona 2: Madina (31 yosh, Olmaota, Qozog'iston) — Kichik Biznes Egasi / Onlayn Do'kon**
   - *Foydalanish holati:* Buyurtmalarni yetkazib berish vaqtlari, ta'minotchilar bilan to'lovlar, xodimlar nazorati.
   - *Ehtiyoji:* 2024-yilgi yangi yagona UTC+5 vaqti bo'yicha aniq eslatmalar, takrorlanuvchi to'lovlar uchun RRULE (har oyning 5-sanasida), rus va qozoq tillarida interfeys.
   - *To'lov qobiliyati:* Kichik biznes qulayligi uchun Kaspi QR yoki Telegram Stars orqali Pro versiyani sotib olishga tayyor.

3. **Persona 3: Jamshid (20 yosh, Samarqand, O'zbekiston) — Universitet Talabasi**
   - *Foydalanish holati:* Dars jadvallari, oraliq nazorat muddatlari, repetitor darslari.
   - *Ehtiyoji:* Oddiy va tushunarli o'zbek tilidagi lotin yozuvi, arzon/bepul xizmat.
   - *Qurilma & Tarmoq:* Byudjetli Android qurilma, viloyat bo'ylab harakatlanganda sekin 3G internet. Mini App sekin ochilganda botning **Fallback FSM Chat rejimida** vazifalarni yaratadi va boshqaradi.

4. **Persona 4: Aybek (35 yosh, Bishkek, Qirg'iziston) — Savdo Menejeri**
   - *Foydalanish holati:* Hamkorlar bilan muzokaralar, mintaqaviy safarlar (Toshkent-Bishkek-Olmaota).
   - *Ehtiyoji:* Qirg'izistonning **UTC+6** vaqt zonasiga mos aniq hisob-kitob, O'zbekiston/Qozog'istondagi hamkorlar bilan soat farqini hisobga olish, tinchlik soatlari (DND) orqali tunda bezovta bo'lmaslik.

### 1.3. Biznes Maqsadlari va Ko'rsatkichlar (KPIs)
- **Foydalanuvchilar qamrovi (Acquisition):** Dastlabki 6 oyda O'rta Osiyo bo'ylab 150 000+ faol oylik foydalanuvchini (MAU) jalb qilish.
- **Ushlab qolish darajasi (Retention):** 30 kunlik ushlab qolish ko'rsatkichi (D30 Retention) $\ge 35\%$.
- **Kunlik Faollik (DAU/MAU nisbati):** $\ge 40\%$ (foydalanuvchilar har kuni reja tuzishi va eslatmalar bilan o'zaro aloqada bo'lishi).
- **Monetizatsiya konversiyasi:** Bepul foydalanuvchilarning kamida 2.5-4% qismini Premium obunaga (Telegram Stars, Click, Payme, Kaspi) aylantirish.

### 1.4. Texnik Maqsadlar va Arxitektura Prinsiplari
- **100% Bepul Serverless Infratuzilma:** Server xarajatlari $0/oy bo'lib, Cloudflare Workers (Backend API/Bot), Cloudflare Pages (Mini App CDN), Supabase (PostgreSQL) va Cloudflare Cron Triggers asosida quriladi.
- **Sub-Soniya Javob Tezligi:** Telegram webhooklariga javob berish $< 500$ ms, Mini App boshlang'ich yuklanishi (FCP) $< 1.2$ s.
- **Kriptografik Xavfsizlik:** Mini App orqali yuboriladigan barcha ma'lumotlar Telegram bot tokeniga asoslangan `HMAC-SHA256` orqali tekshiriladi (Zero Trust).
- **Vaqt Aniqligi:** Har qanday sharoitda eslatmalarning belgilangan muddatdan chetlanishi $\pm 60$ soniyadan oshmasligi ta'minlanadi.

---

## 2. Telegram Bot Xabarlar Mantig'i va Buyruqlar Tizimi

Telegram bot foydalanuvchi bilan aloqa o'rnatuvchi boshlang'ich darvoza (entry point) hisoblanadi. Bot foydalanuvchi bilan asinxron xabarlar va interaktiv inline tugmalar orqali muloqot qiladi.

### 2.1. Bot Buyruqlari Arxitekturasi va Standart Menyu
Bot ishga tushirilganda Telegram Bot API ning `setMyCommands` metodi yordamida quyidagi 6 ta standart buyruq foydalanuvchi interfeysiga joylashtiriladi:

```json
[
  {"command": "start", "description": "🚀 Botni ishga tushirish va boshlash"},
  {"command": "today", "description": "📅 Bugungi vazifalar ro'yxati"},
  {"command": "tasks", "description": "📋 Barcha faol vazifalar"},
  {"command": "add", "description": "➕ Yangi vazifa qo'shish (tezkor)"},
  {"command": "settings", "description": "⚙️ Sozlamalar (til, vaqt zonasi)"},
  {"command": "help", "description": "ℹ️ Yordam va qo'llanma"}
]
```

Telegram chat oynasining pastki chap burchagida doimiy ko'rinib turuvchi Menyu Tugmasi (`MenuButtonWebApp`) o'rnatiladi:
- **Turi:** `web_app`
- **Tugma matni:** `📱 Vazifalarim`
- **URL:** `https://tma.vazifabot.uz/`

### 2.2. Buyruqlarning Batafsil Ishlash Ssenariylari

#### 1. `/start` [param] — Ro'yxatdan O'tish va Deep Linking
Foydalanuvchi botga kirganda quyidagi mantiqiy qadamlar bajariladi:
1. Foydalanuvchining Telegram profili (`telegram_id`, `first_name`, `last_name`, `username`, `language_code`) olinadi.
2. Bazada foydalanuvchi mavjudligi tekshiriladi:
   - Mavjud bo'lmasa: `users` jadvaliga yangi qator kiritiladi. Boshlang'ich til sifatida Telegram interfeys tili, vaqt zonasi sifatida esa standart `Asia/Tashkent` o'rnatiladi.
   - Mavjud bo'lsa: uning profili yangilanadi (`last_seen`).
3. **Deep Linking parametrini tekshirish:**
   - Agar `/start task_<uuid>` kelsa: tizim to'g'ridan-to'g'ri ko'rsatilgan vazifani qidiradi va foydalanuvchiga vazifa kartochkasi hamda `[ 📱 Mini App'da ochish ]` inline tugmasini chiqaradi.
   - Agar `/start ref_<user_id>` kelsa: yangi foydalanuvchi taklif etuvchi hisobiga biriktiriladi va ikkala foydalanuvchiga referal bonus (masalan, 7 kunlik Premium sinov muddati) beriladi.
   - Agar parametr bo'lmasa: standart samimiy xush kelibsiz xabari yuboriladi.

**Xush kelibsiz xabari shabloni (O'zbekcha lotin):**
```
Assalomu alaykum, {first_name}! 👋

"Aqlli Vazifalar va Eslatmalar" tizimiga xush kelibsiz!
Ushbu bot orqali siz barcha rejalaringizni bir joyga to'plashingiz, muhim eslatmalarni o'z vaqtida olishingiz va kunlik unumdorligingizni oshirishingiz mumkin.

🌐 Sizning vaqt mintaqangiz: {timezone} (UTC+5)
Tilni yoki vaqtni o'zgartirish uchun: /settings

Quyidagi tugma orqali qulay vizual interfeysni oching:
```
**Inline tugmalar:**
```
┌───────────────────────────────────────────────────┐
│       📱 Vazifalarim (Mini App'ni Ochish)         │
├─────────────────────────┬─────────────────────────┤
│    ➕ Yangi vazifa      │      📅 Bugungi reja    │
└─────────────────────────┴─────────────────────────┘
```

#### 2. `/today` — Bugungi Vazifalar Xulosasi
Foydalanuvchining tanlangan mahalliy vaqt zonasi bo'yicha bugungi kunning `00:00:00` dan `23:59:59` gacha bo'lgan barcha vazifalarini jamlaydi.
- Vazifalar soni, bajarilganlar va qolganlar nisbati hisoblanadi.
- Progress vizual indikatori yaratiladi (masalan: `[▓▓▓▓░░░░░░] 40%`).
- Vazifalar vaqt tartibida ro'yxat qilinadi.

**Xabar shabloni:**
```
📅 Bugungi rejangiz ({bugungi_sana}):
Progress: {bajarilgan}/{jami} bajarildi ({foiz}%) {progress_bar}

⏳ Kutilayotgan ishlar:
1. 🕒 10:30 — Mijoz bilan uchrashuv [💼 Ish] 🔴
2. 🕒 14:00 — Bankka to'lov qilish [💳 Moliya] 🟡
3. 🕒 19:30 — Fitnes mashg'uloti [🏃 Sport] 🟢

✅ Bajarilganlar:
4. ~~08:00 — Ertalabki badantarbiya~~

Rejani to'liq boshqarish uchun Mini App'ni oching:
```
**Inline tugmalar:**
```
┌───────────────────────────────────────────────────┐
│           📱 Mini App'da to'liq ko'rish           │
├─────────────────────────┬─────────────────────────┤
│     ➕ Vazifa qo'shish  │     🔄 Yangilash        │
└─────────────────────────┴─────────────────────────┘
```

#### 3. `/tasks` — Barcha Faol Vazifalar va Sahifalash (Pagination)
Foydalanuvchining barcha `pending` va `overdue` holatidagi vazifalarini sahifalangan ko'rinishda (har bir sahifada 5 tadan) chiqaradi.
- Har bir element yonida tezkor bajarish tugmasi bo'ladi: `[✅ 1]`, `[✅ 2]`, `[✅ 3]`.
- Sahifalarni almashtirish uchun `[⬅️ Oldingi]` va `[Keyingi ➡️]` tugmalari mavjud.
- Bajarish tugmasi bosilganda server vazifani `completed` holatiga o'tkazadi va xabarni inline yangilaydi (Telegram `editMessageText`).

#### 4. `/add` — Tezkor Vazifa Yaratish
Foydalanuvchi bir qatorda vazifa nomi va vaqtini kiritishi mumkin:
- Masalan: `/add Ertaga soat 16:00 da hisobotni topshirish`
- Bot NLP Regex tahlilchisi orqali matndan sanani, vaqtni va vazifa nomini ajratib oladi, vazifani bazaga saqlaydi va eslatmani rejalashtiradi.
- Agar foydalanuvchi faqat `/add` deb yozsa va qo'shimcha parametr bermasa, bot avtomatik ravishda **Fallback Chat FSM Rejimini** faollashtiradi.

#### 5. `/settings` — Foydalanuvchi Sozlamalari
Foydalanuvchining shaxsiy preferensiyalarini tahrirlash uchun inline menyu taqdim etiladi:
```
⚙️ Sozlamalar menyusi:

Hozirgi sozlamalaringiz:
• Til: O'zbekcha (Lotin) 🇺🇿
• Vaqt zonasi: Asia/Tashkent (UTC+5)
• Tungi tinchlik rejimi: Yoqilgan (23:00 — 07:00)
• Premium maqomi: Bepul (Free Plan)

O'zgartirish uchun quyidagilardan birini tanlang:
```
**Inline tugmalar:**
```
┌─────────────────────────┬─────────────────────────┐
│     🌐 Tilni tanlash    │   🕒 Vaqt mintaqasi     │
├─────────────────────────┼─────────────────────────┤
│   🔕 Tinchlik vaqti     │   💎 Premium obuna      │
└─────────────────────────┴─────────────────────────┘
```

#### 6. `/help` — Yordam va Qo'llanma
Botdan foydalanish bo'yicha to'liq qo'llanma, NLP buyruqlari sintaksisi misollari va texnik qo'llab-quvvatlash xizmati (`@vazifabot_support`) havolasi aks etadi.

---

### 2.3. Deep Linking Mantig'i
Loyiha Telegram platformasining rasmiy Deep Linking mexanizmini to'liq qo'llab-quvvatlaydi. Foydalanuvchi bot xabaridagi yoki tashqi chatdagi havolani bosganda, Telegram to'g'ridan-to'g'ri tegishli kontekstni ochadi.

1. **Telegram Mini App ichiga to'g'ridan-to'g'ri o'tish (Direct TMA Launch):**
   - Format: `https://t.me/<bot_username>/<app_short_name>?startapp=task_<uuid>`
   - Telegram protokoli: `tg://resolve?domain=<bot_username>&appname=<app_short_name>&startapp=task_<uuid>`
   - **TMA ishlash mantig'i:** Mini App yuklanganda `window.Telegram.WebApp.initDataUnsafe.start_param` parametrini o'qiydi. Agar parametr `task_<uuid>` formatida bo'lsa, Mini App asosiy dashboard o'rniga o'sha ko'rsatilgan vazifaning tahrirlash modalini ochadi.
2. **Yangi vazifa yaratish oynasini ochish:**
   - Format: `https://t.me/<bot_username>/<app_short_name>?startapp=create`
   - Ushbu havola bosilganda TMA darhol bo'sh vazifa yaratish formasini to'liq ekranda ochadi.
3. **Xatolik holatlari (Edge Case):**
   - Agar uzatilgan `uuid` bazada topilmasa yoki o'chirilgan bo'lsa, TMA interfeysida xatolik toast xabari chiqadi (*"Vazifa topilmadi yoki o'chirilgan"*) va foydalanuvchi xavfsiz tarzda Asosiy Dashboard'ga yo'naltiriladi.

---

### 2.4. Fallback Chat FSM Mode (Suhbat Asosidagi Matnli Rejim)
O'rta Osiyo hududlarida ba'zi foydalanuvchilar qishloq joylarida sekin internet (EDGE/3G) orqali ulanishi yoki eski rusumdagi smartfonlardan foydalanishi mumkin. Bunday holatlarda og'ir veb-interfeys yuklanmasligi xavfi mavjud. Shu sababli bot to'liq avtonom **Finite State Machine (FSM)** rejimiga ega.

FSM holat mashinasi quyidagi holatlar ketma-ketligini boshqaradi:

```
[IDLE] ──(/add)──> [STATE_ADD_TITLE]
                        │
                  (nomi kiritildi)
                        │
                        ▼
               [STATE_ADD_DATETIME]
                        │
                  (vaqt tanlandi)
                        │
                        ▼
               [STATE_ADD_PRIORITY]
                        │
                  (ustuvorlik tanlandi)
                        │
                        ▼
               [STATE_ADD_CATEGORY]
                        │
                  (toifa tanlandi)
                        │
                        ▼
               [STATE_ADD_CONFIRM] ──(Saqlandi)──> [IDLE]
```

**FSM Bosqichlarining Batafsil Ssenariysi:**
1. **Holat 1: `STATE_ADD_TITLE`**
   - Bot xabari: *"Yangi vazifangiz nomini yozing (Bekor qilish uchun /cancel bosing):"*
   - Foydalanuvchi kiritadi: `"Avtomobilni texnik ko'rikdan o'tkazish"`
   - Tekshiruv: Matn uzunligi 3 dan 255 belgigacha bo'lishi shart.
2. **Holat 2: `STATE_ADD_DATETIME`**
   - Bot xabari: *"Vazifa muddatini qachonga belgilaymiz? Quyidagilardan birini bosing yoki matn sifatida yozing (masalan: Ertaga 15:00):"*
   - Inline tugmalar: `[📅 Bugun 18:00]`, `[📅 Ertaga 10:00]`, `[Indin 12:00]`, `[⏳ Muddatsiz]`
   - Foydalanuvchi tanlaydi yoki qo'lda yozadi. Matn NLP tahlilchidan o'tkaziladi.
3. **Holat 3: `STATE_ADD_PRIORITY`**
   - Bot xabari: *"Ustuvorlik darajasini tanlang:"*
   - Inline tugmalar:
     - `[🟢 Past]`
     - `[🟡 O'rta (Standart)]`
     - `[🔴 Yuqori]`
     - `[🔥 Shoshilinch]`
4. **Holat 4: `STATE_ADD_CATEGORY`**
   - Bot xabari: *"Toifani tanlang:"*
   - Inline tugmalar: Foydalanuvchining mavjud toifalari ko'rsatiladi: `[💼 Ish]`, `[🏠 Shaxsiy]`, `[🚗 Avto]`, `[+ Toifasiz]`.
5. **Holat 5: `STATE_ADD_CONFIRM`**
   - Bot barcha kiritilgan ma'lumotlarni kartochka ko'rinishida chiqaradi va tasdiqlashni so'raydi:
     ```
     Tasdiqlaysizmi?
     📌 Nomi: Avtomobilni texnik ko'rikdan o'tkazish
     📅 Muddati: Ertaga, 15:00 (Asia/Tashkent)
     🔴 Ustuvorlik: Yuqori
     🚗 Toifa: Avto
     ⏰ Eslatma: 15 daqiqa oldin va aynan vaqtida
     ```
   - Tugmalar: `[✅ Saqlash]`, `[❌ Bekor qilish]`
6. **Bekor qilish va Taymaut:**
   - Foydalanuvchi istalgan bosqichda `/cancel` deb yozsa, sessiya to'xtatiladi va holat `IDLE` ga qaytariladi.
   - Agar foydalanuvchi 15 daqiqa davomida javob bermasa, FSM sessiyasi avtomatik yopiladi va resurslar bo'shatiladi.

---

### 2.5. Quick Add NLP Regex Tahlilchisi
Tezkor kiritish funksiyasi foydalanuvchiga hech qanday tugmalarsiz, bir jumlada tabiiy tilda vazifa yaratish imkonini beradi. Tahlilchi O'zbek (lotin va kirill) hamda Rus tillaridagi maxsus temporal (vaqtga oid) leksikani taniydi.

#### Regex Patternlar Matritsasi:

| Maqsad | O'zbekcha Pattern (Lotin / Kirill) | Ruscha Pattern | Aniqlanadigan Qiymat |
|---|---|---|---|
| Nisbiy kunlar | `\b(bugun\|бугун)\b` | `\b(сегодня)\b` | Joriy sana ($D_0$) |
| Ertangi kun | `\b(ertaga\|эртага)\b` | `\b(завтра)\b` | Ertangi sana ($D_0 + 1$) |
| Indingi kun | `\b(indin\|индин\|ertadan keyin)\b` | `\b(послезавтра)\b` | Indingi sana ($D_0 + 2$) |
| Hafta kunlari | `\b(dushanba\|seshanba\|chorshanba\|payshanba\|juma\|shanba\|yakshanba)\b` | `\b(понедельник\|вторник\|среда\|четверг\|пятница\|суббота\|воскресенье)\b` | Eng yaqin kelayotgan hafta kuni sanasi |
| Aniq soat va daqiqa | `(?:soat\s+\|\b)(\d{1,2})[:.-](\d{2})(?:\s*da\|\b)` | `(?:в\s+)?(\d{1,2})[:.-](\d{2})` | Soat $H$, Daqiqa $M$ |
| Faqat soat | `(?:soat\s+)(\d{1,2})(?:\s*da\|\b)` | `(?:в\s+)(\d{1,2})(?:\s*часов\|\s*ч)?` | Soat $H$, Daqiqa 00 |
| Takrorlanish | `\b(har kuni\|ҳар куни)\b` | `\b(каждый день\|ежедневно)\b` | `FREQ=DAILY;INTERVAL=1` |
| Haftalik takror | `\bhar\s+(dushanba\|...\|yakshanba)\b` | `\bкаждый\s+(понедельник\|...)\b` | `FREQ=WEEKLY;BYDAY=...` |

#### Parsing Algoritmi Qadamlari:
1. **Kiruvchi satrni tozalash va normallashtirish:** Katta-kichik harflar tenglashtiriladi (lowercase), keraksiz tinish belgilari olib tashlanadi.
2. **Temporal tokenlarni qidirish:** Sanani va vaqtni bildiruvchi tokenlar yuqoridagi regex orqali aniqlanadi.
3. **Vaqtni hisoblash:** Foydalanuvchining profildagi vaqt mintaqasi (`timezone`) asosida mahalliy sana va vaqt obyektiga aylantiriladi.
4. **O'tib ketgan vaqt tekshiruvi (Overdue prevention):** Agar foydalanuvchi soat 17:00 da turib: `"Soat 11:00 da nonushta qilish"` deb yozsa, tizim 11:00 o'tib ketganini ko'radi va vazifani avtomatik ravishda **ertangi kun soat 11:00 ga** belgilaydi hamda foydalanuvchini ogohlantiradi.
5. **Vazifa sarlavhasini ajratish:** Aniqlangan temporal tokenlar umumiy jumlalardan qirqib olinadi, qolgan qismi toza sarlavha (`title`) sifatida saqlanadi.
   - *Misol:* `"Ertaga soat 15:30 da Zubeyr bilan shartnoma imzolash"`
   - *Ajratilgan muddat:* Ertangi kun, 15:30.
   - *Ajratilgan sarlavha:* `"Zubeyr bilan shartnoma imzolash"`.

---

## 3. Telegram Mini App (TMA) Sahifalari va UI/UX Interfeysi

Telegram Mini App ilovaning asosiy boshqaruv markazi hisoblanadi. U Telegram WebApp ekotizimiga 100% integratsiya qilingan holda native mobil ilovalar darajasidagi tajribani (60 FPS animatsiyalar, haptik tebranish, tungi rejim) taqdim etadi.

### 3.1. Telegram WebApp Native SDK Integratsiyasi
Mini App `@telegram-apps/sdk` yoki rasmiy `Telegram.WebApp` obyekti bilan chuqur integratsiya qilinadi:

1. **Viewport va Fullscreen boshqaruvi:**
   - Ilova ishga tushishi bilanoq `Telegram.WebApp.ready()` va `Telegram.WebApp.expand()` buyruqlari chaqiriladi.
   - Telegram Bot API 8.0+ versiyalarida to'liq ekranni egallash uchun `Telegram.WebApp.requestFullscreen()` chaqiriladi.
   - Ekranni pastga tortganda ilovaning bexosdan yopilib ketishining oldini olish uchun `Telegram.WebApp.disableVerticalSwipes()` funksiyasi majburiy yoqiladi.
2. **Telegram Mavzusi (ThemeParams) bilan Moslashuv:**
   - Ilova Telegram mijozining ranglar sxemasiga (Dark / Light) to'liq bo'ysunadi.
   - CSS o'zgaruvchilari Telegram parametrlaridan oziqlanadi:
     ```css
     :root {
       --tg-color-bg: var(--tg-theme-bg-color, #ffffff);
       --tg-color-text: var(--tg-theme-text-color, #1c1c1e);
       --tg-color-hint: var(--tg-theme-hint-color, #8e8e93);
       --tg-color-link: var(--tg-theme-link-color, #007aff);
       --tg-color-button: var(--tg-theme-button-color, #2481cc);
       --tg-color-button-text: var(--tg-theme-button-text-color, #ffffff);
       --tg-color-secondary-bg: var(--tg-theme-secondary-bg-color, #f2f2f7);
     }
     ```
3. **Haptik Qayta Aloqa (Haptic Feedback):**
   - Vazifa checkbox'i bosilganda: `Telegram.WebApp.HapticFeedback.notificationOccurred('success')`
   - Vazifa o'chirilganda: `Telegram.WebApp.HapticFeedback.notificationOccurred('warning')`
   - Sahifa almashtirilganda yoki filtr bosilganda: `Telegram.WebApp.HapticFeedback.impactOccurred('light')`
   - Xatolik yuz berganda: `Telegram.WebApp.HapticFeedback.notificationOccurred('error')`
4. **Native Tugmalar (MainButton va BackButton):**
   - Asosiy dashboard'da `BackButton` yashiriladi.
   - Ichki sahifalarga (Taqvim, Sozlamalar, Vazifa tahrirlash) o'tganda `BackButton.show()` yoqiladi va bosilganda oldingi sahifaga qaytaradi.
   - Vazifa yaratish/tahrirlash modali ochilganda `MainButton.setText("SAQLASH").show()` yoqiladi va foydalanuvchi kiritishini bitta bosishda saqlaydi.
5. **Kriptografik Autentifikatsiya (initData):**
   - Barcha backend so'rovlarida `Authorization: tma <raw_initData>` sarlavhasi yuboriladi. Backend `hash` qiymatini bot tokeni orqali tekshirmaguncha hech qanday ma'lumot qaytarmaydi.

---

### 3.2. TMA 6 Asosiy Sahifasining Batafsil Tuzilishi

```
┌─────────────────────────────────────────────────────────────┐
│                 TELEGRAM MINI APP ROUTER                    │
├──────────────┬──────────────┬──────────────┬────────────────┤
│ 1. Dashboard │ 2. TaskModal │ 3. Calendar  │ 4. Categories  │
├──────────────┴──────────────┼──────────────┴────────────────┤
│ 5. User Settings            │ 6. Premium Subscription       │
└─────────────────────────────┴───────────────────────────────┘
```

#### Sahifa 1: Asosiy Dashboard (Bosh Sahifa)
- **Header (Yuqori panel):**
  - Foydalanuvchi avatari, ismi va salomlashish matni.
  - Joriy sana va vaqt zonasi indikatori (masalan: `Toshkent, UTC+5`).
  - Bildirishnoma qo'ng'irog'i (faol eslatmalar soni bilan badge).
- **Kunlik Progress Vidjeti (Daily Progress Card):**
  - Vizual aylanma (circular) yoki chiziqli progress bar.
  - Matn: *"Bugungi reja: 5 ta vazifadan 3 tasi bajarildi (60%)"*.
  - Motivatsion qisqa iboralar (*"Ajoyib ketmoqdasiz! 🔥"*).
- **Tezkor Filtr Tablari (Segmented Filter Tabs):**
  - `[ Barchasi ]` | `[ Bugun ]` | `[ Kelgusi ]` | `[ Kechikkan (Overdue) ]`
  - Har bir tab yonida tegishli vazifalar soni aks etadi (masalan: `Kechikkan (2)` qizil rangda).
- **Vazifalar Ro'yxati (Task Cards List):**
  - Kartochka tarkibi:
    - Dumaloq checkbox (bosinganda animatsiya va zarbli haptik).
    - Sarlavha (bajarilganda ustiga chiziladi va xiralashadi).
    - Muddat vaqti va eslatma belgisi: `⏰ 14:00 (15 daqiqa oldin)`.
    - Toifa tegi (masalan: `💼 Ish` moviy fonda, `💊 Sog'liq` qizil fonda).
    - Ustuvorlik indikatori: Qizil (Yuqori), Sariq (O'rta), Yashil (Past).
  - Mobil surish amallari (Swipe Actions):
    - O'ngga surish (Swipe Right) $\rightarrow$ Vazifani tezkor bajarish (`Done`).
    - Chapga surish (Swipe Left) $\rightarrow$ Eslatmani 1 soatga surish yoki o'chirish.
- **Floating Action Button (FAB):**
  - Ekranning pastki o'ng burchagida joylashgan yorqin `+` tugmasi. Bosilganda Vazifa Yaratish Modali ochiladi.

#### Sahifa 2: Vazifa Yaratish va Tahrirlash Modali (Task Modal)
- **Sarlavha (Title):** Majburiy matn maydoni (1-255 belgi), tozalash tugmasi bilan.
- **Batafsil Tavsif (Description):** Ko'p qatorli matn (Markdown formatlash va havolalarni qo'llab-quvvatlaydi).
- **Muddat Sanasi va Vaqti Picker:**
  - Tezkor sana tugmalari: `[Bugun]`, `[Ertaga]`, `[Dam olish kuni]`, `[Taqvimdan...]`.
  - Soat va daqiqa tanlash mexanizmi (24-soatlik format).
  - Switch: *"Kun bo'yi davom etadi"* (All-day task).
- **Eslatma Oraliqlari (Multi-Stage Reminder Selector):**
  - Ko'p tanlovli ro'yxat (bir vaqtning o'zida bir nechta eslatma qo'yish mumkin):
    - `[x] Aynan belgilangan vaqtda (T=0)`
    - `[x] 15 daqiqa oldin`
    - `[ ] 1 soat oldin`
    - `[ ] 1 kun oldin (24 soat)`
- **Ustuvorlik Darajasi (Priority Selector):**
  - 4 bosqichli tanlov: `Past 🟢`, `O'rta 🟡`, `Yuqori 🔴`, `Shoshilinch 🔥`.
- **Toifa Biriktirish:**
  - Foydalanuvchi toifalari ro'yxatidan tanlash yoki modal ichidan yangi toifa ochish.
- **Takrorlanish Qoidasi (RRULE Selector):**
  - Variantlar: `Takrorlanmasin`, `Har kuni`, `Ish kunlari (Dush-Juma)`, `Har hafta`, `Har oy`, `Maxsus interval`.
- **Harakat Tugmalari:**
  - Telegram `MainButton`: *"Saqlash"*.
  - Agar tahrirlash rejimi bo'lsa: pastda qizil rangli *"Vazifani o'chirish"* tugmasi (tasdiqlash bilan).

#### Sahifa 3: Taqvimi va Timeline Sahifasi (Calendar & Timeline)
- **Gorizontal Hafta Lentasi (Horizontal Week Strip):**
  - Foydalanuvchi joriy haftani kunlar bo'yicha varoqlashi mumkin.
  - Har bir kun katakchasi ostida o'sha kundagi vazifalar sonini bildiruvchi rangli nuqtalar (dots) aks etadi.
- **Oylik Taqvim Gridi (Monthly Grid Toggle):**
  - Butun oyni ko'rish tugmasi bosilganda klassik 30/31 kunlik kalendar ochiladi.
- **Kunlik Soatlik Jadval (Hourly Timeline):**
  - Vertikal vaqt o'qi: `08:00`, `09:00`, `10:00`, ..., `23:00`.
  - Vazifalar o'z vaqt oralig'iga mos keluvchi bloklar sifatida ko'rsatiladi (Google Calendar / Apple Reminders uslubida).
  - Foydalanuvchi istalgan bo'sh soat blokini bosganda, o'sha soat avtomatik to'ldirilgan holda yangi vazifa yaratish modali ochiladi.

#### Sahifa 4: Toifalar va Teglar Boshqaruvi (Categories & Tags)
- **Toifalar Ro'yxati:**
  - Har bir toifa yonida uning emoji belgisi, nomi, rang doirasi va unga tegishli faol vazifalar soni ko'rsatiladi.
- **Yangi Toifa Yaratish Modali:**
  - Toifa nomi (masalan: `Sport`, `Moliya`, `Uy yumushlari`).
  - Emoji tanlash picker'i (100+ ommabop emojilar).
  - Ranglar palitrasi: 12 ta zamonaviy pastel ranglar (HEX kodlari bilan).
- **Toifani O'chirish Himoyasi:**
  - Agar toifada faol vazifalar mavjud bo'lsa, tizim foydalanuvchiga tanlov beradi:
    - Variant A: *"Vazifalarni saqlab qolish (Toifasiz qilish)"*
    - Variant B: *"Barcha vazifalar bilan birga o'chirish"*

#### Sahifa 5: Foydalanuvchi Sozlamalari (User Settings)
- **Til Tanlash (Language):**
  - `O'zbekcha (Lotin)` 🇺🇿
  - `Ўзбекча (Кирилл)` 🇺🇿
  - `Русский` 🇷🇺
  - `English` 🇬🇧
- **Vaqt Mintaqasi (Timezone Selector):**
  - Brauzer orqali avtomatik aniqlash tugmasi (`Intl.DateTimeFormat`).
  - O'rta Osiyo poytaxtlari ro'yxatidan qo'lda tanlash (Toshkent, Samarqand, Olmaota, Bishkek, Dushanbe, Ashxobod).
- **Tungi Tinchlik Rejimi (Quiet Hours / DND):**
  - Yoqish / O'chirish switcheri.
  - Tinchlik boshlanish vaqti (Standart: `23:00`).
  - Tinchlik tugash vaqti (Standart: `07:00`).
  - Switch: *"Shoshilinch (Urgent) vazifalarga tunda ham ovozli ruxsat berish"*.
- **Eslatma Standartlari (Default Preferences):**
  - Standart eslatma oraliqlari (yangi vazifa yaratilganda avtomatik tanlanadigan offset).
- **Ma'lumotlar Eksporti va Maxfiylik:**
  - Barcha vazifalarni JSON yoki CSV formatda yuklab olish imkoniyati.
  - Ma'lumotlarni butunlay tozalash (GDPR muvofiqligi).

#### Sahifa 6: Premium Obuna Sahifasi (Premium Upgrade)
- **Tariflar Taqqoslash Jadvali (Feature Matrix):**
  - *Bepul (Free):* Maksimal 30 ta faol vazifa, 3 ta toifa, bitta bosqichli eslatma.
  - *Premium:* Cheksiz vazifalar va toifalar, 5 bosqichli ogohlantirish quvuri, murakkab RRULE takrorlanishlar, Ovozli xabarni AI orqali vazifaga aylantirish (Voice-to-Task), kalendarlarni sinxronlash (.ics eksport).
- **Tarif Davrlari:**
  - 1 oylik obuna
  - 6 oylik obuna (15% chegirma)
  - 1 yillik obuna (30% chegirma)
- **To'lov Usullari:**
  - `⭐ Telegram Stars (XTR)` — Bot API orqali to'g'ridan-to'g'ri ilova ichida to'lov.
  - `🇺🇿 Click / Payme / Uzum` — O'zbekiston bank kartalari (Uzcard / Humo) uchun.
  - `🇰🇿 Kaspi QR` — Qozog'iston foydalanuvchilari uchun.

---

## 4. Vazifalar Hayot Sikli va Ma'lumotlar Modeli

### 4.1. Vazifa Holatlari Mashinasi (5-State FSM)
Har bir vazifa o'z hayot davomida qat'iy belgilangan 5 holatdan birida bo'ladi:
1. `pending` (Kutilmoqda) — Vazifa yaratilgan, muddati hali kelmagan.
2. `in_progress` (Jarayonda) — Foydalanuvchi vazifani bajarishni boshlagan.
3. `completed` (Bajarildi) — Vazifa muvaffaqiyatli yakunlangan.
4. `overdue` (Kechikkan) — Belgilangan muddat o'tib ketgan, lekin vazifa bajarilmagan.
5. `cancelled` (Bekor qilindi) — Foydalanuvchi vazifani bekor qilgan yoki arxivlagan.

```
                   ┌──────────────┐
                   │   Yaratildi  │
                   └──────┬───────┘
                          │
                          ▼
                   ┌──────────────┐
     ┌────────────▶│   PENDING    │◀────────────┐
     │             └──────┬───────┘             │
     │               │    │   │                 │
     │  (Boshlash)   │    │   │ (Muddat o'tdi)  │ (Qayta tiklash)
     │   ┌───────────┘    │   └──────────┐      │
     │   ▼                │              ▼      │
┌──────────────┐          │       ┌─────────────┴┐
│ IN_PROGRESS  │          │       │   OVERDUE    │
└────────┬─────┘          │       └──────┬───────┘
         │                │              │
         │ (Tugatish)     │ (Tugatish)   │ (Tugatish)
         ▼                ▼              ▼
       ┌───────────────────────────────────┐
       │             COMPLETED             │
       └──────────────────┬────────────────┘
                          │
                          ▼ (Arxivlash/Bekor qilish)
                   ┌──────────────┐
                   │  CANCELLED   │
                   └──────────────┘
```

#### Holatlar O'tish Matritsasi (State Transition Table):

| Joriy Holat | Hodisa (Event) | Yangi Holat | Shartlar va Qoidalar |
|---|---|---|---|
| `pending` | `START_WORK` | `in_progress` | Foydalanuvchi vazifani boshlaganda |
| `pending` | `DUE_DATE_PASSED` | `overdue` | Server vaqti vazifa muddatidan o'tganda ($T > due\_datetime$) |
| `pending` | `COMPLETE` | `completed` | Foydalanuvchi "Bajarildi" deb belgilaganda |
| `pending` | `CANCEL` | `cancelled` | Foydalanuvchi vazifani bekor qilganda |
| `in_progress` | `COMPLETE` | `completed` | Ish yakunlanganda |
| `in_progress` | `CANCEL` | `cancelled` | Ish bekor qilinganda |
| `overdue` | `COMPLETE` | `completed` | Kechikkan vazifa nihoyasiga yetganda |
| `overdue` | `RESCHEDULE` | `pending` | Foydalanuvchi muddatni kelajakka surganida |
| `overdue` | `CANCEL` | `cancelled` | Kechikkan vazifa bekor qilinganda |
| `completed` | `REOPEN` | `pending` | Tasodifan bajarildi deb belgilansa, qayta ochish |
| `completed` | `ARCHIVE` | `cancelled` | Tarixni tozalash |

---

### 4.2. RFC 5545 RRULE Takrorlanish Dvigateli
Takrorlanuvchi vazifalar xalqaro **iCalendar RFC 5545** standarti asosida amalga oshiriladi.

#### Qo'llab-quvvatlanadigan Qoidalar Formati:
- **Kunlik:** `FREQ=DAILY;INTERVAL=1` (Har kuni bitta vaqtda)
- **Ish kunlari:** `FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR` (Dushanbadan jumagacha)
- **Haftalik:** `FREQ=WEEKLY;BYDAY=SA` (Har shanba kuni)
- **Oylik:** `FREQ=MONTHLY;BYMONTHDAY=15` (Har oyning 15-sanasida)
- **Interval bilan:** `FREQ=DAILY;INTERVAL=3` (Har 3 kunda bir marta)

#### Takrorlanishni Qayta Ishlash Mantig'i:
1. Foydalanuvchi takrorlanuvchi vazifani `completed` deb belgilagan onda, joriy vazifa bazada `completed` maqomida qoladi (`completed_at = NOW()`).
2. Tizim uning `recurrence_rule` satrini parslash orqali navbatdagi muddat sanasini ($T_{next}$) hisoblab chiqadi.
3. Yangi vazifa yaratiladi:
   - `parent_task_id = current_task.id` (bog'liqlik saqlanadi).
   - `due_datetime = T_{next}`.
   - `status = 'pending'`.
4. Yangi vazifa uchun barcha tegishli ko'p bosqichli eslatmalar (`task_reminders`) avtomatik generatsiya qilinadi.

#### Oylik Muddatlarning Chekka Holati (End-of-Month Edge Case):
Agar vazifa oyning 31-sanasiga belgilangan bo'lsa (`BYMONTHDAY=31`), fevral oyida 31-sana mavjud emas. Tizim RFC 5545 qoidasiga muvofiq, fevralning so'nggi kuniga (kabisa bo'lmagan yili 28-fevral, kabisa yilida 29-fevral) va 30 kunlik oylarda (aprel, iyun, sentabr, noyabr) 30-sanaga avtomatik to'g'rilaydi.

---

### 4.3. Relyatsion PostgreSQL DDL Sxemasi
Ushbu sxema Supabase (PostgreSQL) muhitida to'liq ishlab chiqarish darajasida, indekslar, cheklovlar va kaskadli yaxlitlik bilan loyihalashtirilgan.

```sql
-- Kengaytmalarni yoqish
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 1. Foydalanuvchilar jadvali (users)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    telegram_id BIGINT UNIQUE NOT NULL,
    username VARCHAR(64),
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128),
    language_code VARCHAR(10) NOT NULL DEFAULT 'uz-Latn',
    timezone VARCHAR(64) NOT NULL DEFAULT 'Asia/Tashkent',
    quiet_hours_enabled BOOLEAN NOT NULL DEFAULT TRUE,
    quiet_hours_start TIME NOT NULL DEFAULT '23:00:00',
    quiet_hours_end TIME NOT NULL DEFAULT '07:00:00',
    is_premium BOOLEAN NOT NULL DEFAULT FALSE,
    premium_expires_at TIMESTAMPTZ,
    bot_blocked BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT chk_language_code CHECK (language_code IN ('uz-Latn', 'uz-Cyrl', 'ru', 'en'))
);

-- 2. Toifalar jadvali (categories)
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(64) NOT NULL,
    icon_emoji VARCHAR(16) NOT NULL DEFAULT '📌',
    color_hex VARCHAR(7) NOT NULL DEFAULT '#3390EC',
    order_index INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_user_category_name UNIQUE (user_id, name),
    CONSTRAINT chk_color_hex CHECK (color_hex ~ '^#[0-9A-Fa-f]{6}$')
);

-- 3. Vazifalar jadvali (tasks)
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
    parent_task_id UUID REFERENCES tasks(id) ON DELETE SET NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    priority VARCHAR(16) NOT NULL DEFAULT 'medium',
    status VARCHAR(16) NOT NULL DEFAULT 'pending',
    due_datetime TIMESTAMPTZ, -- Har doim UTC formatda saqlanadi
    is_all_day BOOLEAN NOT NULL DEFAULT FALSE,
    recurrence_rule VARCHAR(255), -- RFC 5545 satri
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT chk_task_priority CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
    CONSTRAINT chk_task_status CHECK (status IN ('pending', 'in_progress', 'completed', 'overdue', 'cancelled'))
);

-- 4. Eslatmalar jadvali (task_reminders)
CREATE TABLE task_reminders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
    trigger_datetime TIMESTAMPTZ NOT NULL, -- UTC formatda jo'natish daqiqasi
    offset_minutes INT NOT NULL DEFAULT 0, -- -1440, -60, -15, 0, 60
    stage VARCHAR(32) NOT NULL DEFAULT 'due_exact',
    status VARCHAR(16) NOT NULL DEFAULT 'scheduled',
    sent_at TIMESTAMPTZ,
    telegram_message_id BIGINT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT chk_reminder_stage CHECK (stage IN ('lead_24h', 'lead_1h', 'lead_15m', 'due_exact', 'overdue_1h', 'snooze')),
    CONSTRAINT chk_reminder_status CHECK (status IN ('scheduled', 'sent', 'acknowledged', 'cancelled', 'failed'))
);

-- 5. Obunalar va to'lovlar jadvali (subscriptions)
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    plan_id VARCHAR(32) NOT NULL, -- 'premium_1m', 'premium_6m', 'premium_1y'
    provider VARCHAR(32) NOT NULL, -- 'telegram_stars', 'click', 'payme', 'kaspi'
    transaction_id VARCHAR(128) UNIQUE NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    currency VARCHAR(8) NOT NULL, -- 'XTR', 'UZS', 'KZT', 'USD'
    status VARCHAR(16) NOT NULL DEFAULT 'active', -- 'active', 'expired', 'refunded'
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT chk_sub_status CHECK (status IN ('active', 'expired', 'refunded'))
);

-- 6. Yuqori unumdorlik indekslari (Indexes for Query Optimization)
CREATE INDEX idx_users_telegram_id ON users(telegram_id);
CREATE INDEX idx_tasks_user_status ON tasks(user_id, status);
CREATE INDEX idx_tasks_due_datetime ON tasks(due_datetime);
CREATE INDEX idx_tasks_category_id ON tasks(category_id);
CREATE INDEX idx_reminders_trigger_status ON task_reminders(trigger_datetime, status) WHERE status = 'scheduled';
CREATE INDEX idx_reminders_task_id ON task_reminders(task_id);
CREATE INDEX idx_subscriptions_user_status ON subscriptions(user_id, status);

-- 7. updated_at avtomatik yangilash trigger funksiyasi
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_timestamp_users
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TRIGGER set_timestamp_categories
BEFORE UPDATE ON categories
FOR EACH ROW EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TRIGGER set_timestamp_tasks
BEFORE UPDATE ON tasks
FOR EACH ROW EXECUTE PROCEDURE trigger_set_timestamp();
```

---

## 5. Vazifani Ogohlantirish (Notification) Jarayoni va Bosqichlari

### 5.1. 5 Bosqichli Ogohlantirish Quvuri (Multi-Stage Pipeline)
Foydalanuvchi muhim ishlarni unutib qoldirmasligi uchun tizim ko'p bosqichli ogohlantirish konveyeridan foydalanadi:

```
Vazifa muddati: [ T = due_datetime ]

  [T - 24 soat]       [T - 1 soat]       [T - 15 daqiqa]       [ T = 0 ]         [T + 1 soat]
        │                   │                   │                  │                  │
        ▼                   ▼                   ▼                  ▼                  ▼
   1-bosqich:          2-bosqich:          3-bosqich:         4-bosqich:         5-bosqich:
  Ertangi reja        Tayyorgarlik        Tezkor diqqat      Aniq vaqt!       Muddati o'tdi!
 (lead_24h, faqat     (lead_1h)           (lead_15m)         (due_exact)      (overdue_1h)
  High/Urgent)
```

1. **1-bosqich: `T - 24 soat` (`lead_24h`):**
   - Faqat yuqori (`high`) va shoshilinch (`urgent`) vazifalar uchun yuboriladi.
   - Maqsad: Ertangi kunga oldindan tayyorgarlik ko'rish.
2. **2-bosqich: `T - 1 soat` (`lead_1h`):**
   - Vazifaga yo'lga chiqish yoki materiallarni yig'ish eslatmasi.
3. **3-bosqich: `T - 15 daqiqa` (`lead_15m`):**
   - Ish stoliga o'tirish yoki uchrashuvga ulanish uchun so'nggi ogohlantirish.
4. **4-bosqich: `T = 0` (`due_exact`):**
   - Asosiy signal: *"Vazifani bajarish vaqti yetdi!"*.
5. **5-bosqich: `T + 1 soat` (`overdue_1h`):**
   - Agar foydalanuvchi vazifani bajarmagan bo'lsa va kechiktirish tugmasini bosmagan bo'lsa, tizim vazifani `overdue` deb belgilaydi va ogohlantiradi: *"Ushbu vazifa muddati o'tdi. Rejani yangilaysizmi?"*.

---

### 5.2. Interaktiv Inline Tugmalar va Xabar Shabloni
Eslatma vaqti kelganda Telegram bot foydalanuvchiga formatlangan xabar va harakat tugmalarini yuboradi.

**Eslatma Xabari Shabloni:**
```
⏰ ESLATMA: {task_title}
━━━━━━━━━━━━━━━━━━━━━━━
📅 Muddat: {formatted_local_time} ({timezone_name})
🏷 Toifa: {category_emoji} {category_name} | {priority_badge}
📝 Izoh: {task_description}

Quyidagi amallardan birini tanlang:
```

**Inline Tugmalar Matritsasi:**
```
┌─────────────────────────┬─────────────────────────┐
│     ✅ Bajarildi        │    💤 15 daqiqa surish  │
├─────────────────────────┼─────────────────────────┤
│    ⏳ 1 soat surish     │    📅 Ertaga qoldirish  │
├─────────────────────────┴─────────────────────────┤
│            📱 Mini App'da ochish                  │
└───────────────────────────────────────────────────┘
```

#### Callback Query Amallari Mantig'i:
- **`✅ Bajarildi` (`cb:done:<task_id>`):**
  - Vazifa statusi `completed` bo'ladi, `completed_at = NOW()`.
  - Kelgusi rejalashtirilgan eslatmalar bekor qilinadi (`status = 'cancelled'`).
  - Xabar inline tahrirlanadi:
    ```
    ~~⏰ ESLATMA: {task_title}~~
    ✅ Bajarildi deb belgilandi! ({completion_time}) 🎉
    ```
  - Tugmalar olib tashlanadi va faqat `[📱 Mini App]` qoldiriladi.
  - Foydalanuvchiga Telegram toasti chiqadi: *"Ajoyib! Vazifa bajarildi 🔥"*.
- **`💤 15 daqiqa surish` (`cb:snooze:<task_id>:15`):**
  - Yangi eslatma yozuvi yaratiladi: `trigger_datetime = NOW() + INTERVAL '15 MINUTES'`.
  - Xabar matni yangilanadi: *"💤 15 daqiqaga kechiktirildi ({new_time} da qayta eslatiladi)"*.
- **`⏳ 1 soat surish` (`cb:snooze:<task_id>:60`):**
  - Yangi eslatma 60 daqiqadan keyinga rejalashtiriladi.
- **`📅 Ertaga qoldirish` (`cb:postpone:<task_id>:tomorrow`):**
  - Vazifaning muddati ertangi kunning ayni shu soatiga ko'chiriladi.

---

### 5.3. Tungi Tinchlik Rejimi (Quiet Hours / DND)
Foydalanuvchining uyqu vaqtida (standart: `23:00` dan `07:00` gacha) bezovta qilinmasligi uchun quyidagi mantiq amal qiladi:
1. Eslatma yuborilishidan oldin foydalanuvchining mahalliy vaqti hisoblanadi.
2. Agar mahalliy vaqt foydalanuvchining `quiet_hours_start` va `quiet_hours_end` oralig'iga to'g'ri kelsa:
   - **Odatiy vazifalar (`low`, `medium`, `high`):** Xabar Telegram API'ga `disable_notification: true` parametri bilan yuboriladi. Xabar foydalanuvchiga tovushsiz va tebranishsiz yetib boradi.
   - **Foydalanuvchi xohishiga ko'ra (Ertalabga kechiktirish varianti):** Agar sozlamalarda belgilangan bo'lsa, eslatma ertalab soat `07:00` ga kechiktiriladi.
   - **Shoshilinch vazifalar (`urgent`):** Agar foydalanuvchi *"Favqulodda vazifalarga tunda ham ruxsat berish"* sozlamasini yoqqan bo'lsa, xabar ovoz bilan yetkaziladi.

---

### 5.4. Telegram Tezlik Cheklovlari (Rate Limits) va Xatoliklarni Boshqarish
Telegram Bot API ning qat'iy cheklovlariga rioya qilish loyiha barqarorligining garovidir:

1. **Telegram API Limitlari:**
   - Global yuborish tezligi: Sekundiga maksimal **30 ta xabar**.
   - Bitta individual chatga: Sekundiga maksimal **1 ta xabar**.
   - Guruhlarga: Daqiqasiga maksimal **20 ta xabar**.
2. **Leaky Bucket Navbat Arxitekturasi:**
   - Barcha jo'natilishi kerak bo'lgan eslatmalar Cron orqali Supabase'dan `FOR UPDATE SKIP LOCKED` yordamida olinadi.
   - Xabarlar sekundiga 25-28 ta qilib navbatga taqsimlanadi (xavfsiz chegara).
3. **HTTP 429 Too Many Requests bilan ishlash:**
   - Agar Telegram'dan `429` xatosi qaytsa, javobdagi `parameters.retry_after` soniyasi o'qiladi va tizim o'sha vaqt mobaynida xabar yuborishni to'xtatib turadi (Exponential Backoff).
4. **Foydalanuvchi botni bloklagan bo'lsa (Error 403 Forbidden):**
   - Agar xabar yuborilganda `403: Bot was blocked by the user` qaytsa, foydalanuvchining bazadagi profiliga `bot_blocked = true` belgisi qo'yiladi.
   - Uning kelgusi barcha rejalashtirilgan eslatmalari to'xtatiladi, bu esa behuda API so'rovlarini bartaraf etadi.

---

## 6. Vaqt Mintaqalari (Timezone) Boshqaruvi

### 6.1. O'rta Osiyo Davlatlari va Vaqt Zonalari Xaritasi
O'rta Osiyo mintaqasida vaqtni boshqarish bo'yicha eng muhim texnik talablar:

| Davlat | Asosiy Shaharlar | IANA Timezone Kodi | UTC Siljishi | Yozgi Vaqt (DST) | Izoh va Tarixiy Qoidalar |
|---|---|---|---|---|---|
| 🇺🇿 **O'zbekiston** | Toshkent, Samarqand, Buxoro, Andijon | `Asia/Tashkent`, `Asia/Samarkand` | **UTC+5** | Mavjud emas | Barcha viloyatlar yagona UTC+5 vaqtida ishlaydi |
| 🇰🇿 **Qozog'iston** | Olmaota, Ostona, Chimkent, Aqtau, Atirau | `Asia/Almaty`, `Asia/Qyzylorda`, `Asia/Oral`, `Asia/Aqtau` | **UTC+5** | Mavjud emas | **2024-yil 1-martdagi davlat islohoti:** Butun Qozog'iston yagona UTC+5 ga o'tdi (eskirgan UTC+6 butunlay bekor qilingan) |
| 🇰🇬 **Qirg'iziston** | Bishkek, O'sh, Jalolobod | `Asia/Bishkek` | **UTC+6** | Mavjud emas | O'rta Osiyodagi yagona UTC+6 davlat |
| 🇹🇯 **Tojikiston** | Dushanbe, Xo'jand, Ko'lob | `Asia/Dushanbe` | **UTC+5** | Mavjud emas | Yagona UTC+5 zonasi |
| 🇹🇲 **Turkmaniston** | Ashxobod, Turkmanboshi, Mary | `Asia/Ashgabat` | **UTC+5** | Mavjud emas | Yagona UTC+5 zonasi |

> **⚠️ KRITIK ISLOHOT OGOHLANTIRISHI (Qozog'iston 2024):**  
> 2024-yil 1-martgacha Olmaota va Ostona shaharlari UTC+6 zonasida bo'lgan. Ko'plab eskirgan operatsion tizimlar va kutubxonalar hamon Olmaotani UTC+6 deb ko'rsatadi. Ushbu loyihada IANA TZDB ning 2024a+ spetsifikatsiyasiga qat'iy rioya qilinadi va butun Qozog'iston hududi **UTC+5** deb hisoblanadi.

---

### 6.2. Vaqtni Saqlash va Konvertatsiya Qilish Matematikasi
1. **Saqlash standarti:** Barcha sanalar ma'lumotlar bazasida qat'iy **UTC** (`TIMESTAMPTZ` yoki ISO-8601 `YYYY-MM-DDTHH:mm:ssZ`) formatida saqlanadi.
2. **Hisoblash formulasi:**
   - Foydalanuvchi Toshkent vaqti (UTC+5) bilan soat `16:30` ga vazifa qo'ydi.
   - Bazaga yoziladigan UTC vaqt:
     $$T_{\text{UTC}} = T_{\text{Local}} - \text{Offset} = 16:30 - 05:00 = 11:30\text{ UTC}$$
   - Agar foydalanuvchi Bishkekda (UTC+6) soat `16:30` ga vazifa qo'ysa:
     $$T_{\text{UTC}} = 16:30 - 06:00 = 10:30\text{ UTC}$$
3. **Trigger tekshiruvi:**
   - Cron eslatma qidirganda har daqiqada:
     ```sql
     SELECT * FROM task_reminders 
     WHERE trigger_datetime <= NOW() AT TIME ZONE 'UTC' 
       AND status = 'scheduled'
     ```
   - Bu arxitektura foydalanuvchining vaqt zonasidan qat'i nazar, barcha eslatmalarni yagona UTC vaqt o'qi bo'yicha xatosiz jo'natishni kafolatlaydi.

---

## 7. Nofunksional Talablar (NFRs)

### 7.1. Tezlik va Kechikish Ko'rsatkichlari (Performance & Latency)
- **Bot Webhook Javob Vaqti:** `< 500 ms`. Telegram serverlariga zudlik bilan `HTTP 200 OK` qaytariladi, xabarni tahlil qilish va yuborish asinxron navbatga (Edge worker background task) o'tkaziladi.
- **Mini App Yuklanish Tezligi (FCP):** 3G va 4G mobil tarmoqlarida First Contentful Paint ko'rsatkichi `< 1.2 soniya`.
- **Statik Paket Hajmi:** Mini App'ning barcha siqilgan (Brotli/Gzip) JS va CSS fayllari umumiy hajmi `< 250 KB`.
- **Eslatma Yetkazish Aniqligi (Precision):** Belgilangan vaqtdan chetlanish $\pm 60$ soniyadan oshmasligi shart (har daqiqalik Edge Cron orqali ta'minlanadi).

### 7.2. Ishonchlilik, Xavfsizlik va Barqarorlik (Reliability & Security)
- **Barqarorlik (Uptime):** Bulutli serverless muhitda 99.5% uzluksiz ishlash ko'rsatkichi.
- **Idempotensiya:** Telegram tomonidan qayta yuborilgan har bir `update_id` keshda tekshiriladi; bitta xabarga ikki marta javob qaytarilmaydi.
- **Telegram WebApp initData Autentifikatsiyasi:** Barcha REST API chaqiruvlarida Telegram bot tokenining HMAC-SHA256 xeshi tekshiriladi. Begona yoki soxtalashtirilgan so'rovlar zudlik bilan `401 Unauthorized` bilan rad etiladi.
- **Tenant Izolatsiyasi (Anti-IDOR):** Har bir SQL so'rovda majburiy ravishda `WHERE user_id = :authenticated_user_id` sharti qo'llaniladi. Foydalanuvchi boshqa shaxsning vazifasini ko'ra olmaydi yoki tahrirlay olmaydi.
- **Graceful Degradation:** Agar Mini App yuklanmasa yoki serverda vaqtinchalik muammo bo'lsa, foydalanuvchi botning Fallback FSM suhbat rejimi orqali barcha vazifalarini uzluksiz boshqarishda davom etadi.

### 7.3. 4 Tilli Mahalliylashtirish (Localization & i18n)
Tizim O'rta Osiyodagi ko'p millatli demografik tuzilmani hisobga olgan holda 4 tilda to'liq faoliyat yuritadi:
1. `uz-Latn` — O'zbek tili (Lotin alifbosi) — Standart til.
2. `uz-Cyrl` — Ўзбек тили (Кирилл ёзуви) — Katta yoshli foydalanuvchilar uchun.
3. `ru` — Русский язык — Qozog'iston, Qirg'iziston va MDH mintaqasi uchun biznes tili.
4. `en` — English — Chet ellik mutaxassislar va ekspatlar uchun.

**Mahalliylashtirish Standartlari:**
- Sanalar formati: `DD.MM.YYYY` (masalan: `10.10.2026`).
- Vaqt formati: 24-soatlik tizim (`15:30`, `09:00`).
- Valyuta formatlari:
  - O'zbekiston: `15 000 so'm`
  - Qozog'iston: `790 ₸`
  - Qirg'iziston: `150 сом`
  - Xalqaro / Telegram: `50 Stars ⭐`

---

## 8. Hujjatni Tasdiqlash va Muvofiqlik
Ushbu Texnik Topshiriq (TZ.md) loyihaning barcha arxitektura, xavfsizlik, ma'lumotlar bazasi va foydalanuvchi interfeysi talablarini to'liq qamrab oladi va keyingi arxitektura (M2), xavfsizlik (M3) hamda monetizatsiya (M4) bosqichlari uchun boshlang'ich texnik asos hisoblanadi.
