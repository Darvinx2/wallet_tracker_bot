import asyncpg

from data.config import DB_CONNECT

pool: asyncpg.Pool = None


async def init_db():
    global pool
    pool = await asyncpg.create_pool(
        **DB_CONNECT,
        min_size=3,
        max_size=5,
    )


async def close_db():
    await pool.close()
