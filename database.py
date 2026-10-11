import os
import asyncio
import asyncpg
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

async def get_connection():
    return await asyncpg.connect(DATABASE_URL)

async def init_db():
    conn = await get_connection()
    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGINT PRIMARY KEY,
                full_name TEXT,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS plans (
                id SERIAL PRIMARY KEY,
                user_id BIGINT REFERENCES users(user_id),
                task_text TEXT NOT NULL,
                task_time TIMESTAMP NOT NULL,
                is_completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
    finally:
        await conn.close()

async def add_or_update_user(user_id: int, full_name: str):
    conn = await get_connection()
    try:
        await conn.execute('''
            INSERT INTO users (user_id, full_name)
            VALUES ($1, $2)
            ON CONFLICT (user_id) DO UPDATE SET full_name = EXCLUDED.full_name;
        ''', user_id, full_name)
    finally:
        await conn.close()

async def add_plan(user_id: int, task_text: str, task_time: datetime):
    conn = await get_connection()
    try:
        return await conn.fetchval('''
            INSERT INTO plans (user_id, task_text, task_time)
            VALUES ($1, $2, $3)
            RETURNING id;
        ''', user_id, task_text, task_time)
    finally:
        await conn.close()

async def get_user_plans(user_id: int):
    conn = await get_connection()
    try:
        return await conn.fetch('''
            SELECT id, task_text, task_time, is_completed
            FROM plans
            WHERE user_id = $1 AND is_completed = FALSE
            ORDER BY task_time ASC;
        ''', user_id)
    finally:
        await conn.close()

async def get_due_plans():
    conn = await get_connection()
    try:
        return await conn.fetch('''
            SELECT id, user_id, task_text, task_time
            FROM plans
            WHERE is_completed = FALSE AND task_time <= (NOW() AT TIME ZONE 'Asia/Tashkent')
            ORDER BY task_time ASC;
        ''')
    finally:
        await conn.close()

async def mark_plan_completed(plan_id: int):
    conn = await get_connection()
    try:
        await conn.execute('''
            UPDATE plans
            SET is_completed = TRUE
            WHERE id = $1;
        ''', plan_id)
    finally:
        await conn.close()
