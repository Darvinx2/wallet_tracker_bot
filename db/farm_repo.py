from db import db_connection


async def get_farm(user_id: int):
    return await db_connection.pool.fetchrow(
        "SELECT id FROM farms WHERE user_id = $1", user_id
    )


async def insert_farm(user_id: int, chain: str, total: float):
    return await db_connection.pool.fetchval(
        "INSERT INTO farms(user_id, chain, total) VALUES($1, $2, $3) RETURNING id",
        user_id,
        chain,
        total,
    )


async def insert_wallet(farm_id: int, chain: str, wallet: str):
    return await db_connection.pool.execute(
        "INSERT INTO farm_wallets(farm_id, chain, wallet) VALUES($1, $2, $3)",
        farm_id,
        chain,
        wallet,
    )


async def get_farm_id(user_id: int):
    return await db_connection.pool.fetchval(
        "SELECT id FROM farms WHERE user_id = $1", user_id
    )


async def get_farm_wallet(user_id: int):
    return await db_connection.pool.fetchrow(
        "SELECT array_agg(wallet) FROM farm_wallets "
        "JOIN farms "
        "ON farms.id = farm_wallets.farm_id "
        "WHERE user_id = $1;",
        user_id,
    )


async def delete_farm(user_id: int):
    return await db_connection.pool.execute(
        "DELETE FROM farms WHERE user_id = $1", user_id
    )


async def update_total(total: float, user_id: int):
    return await db_connection.pool.execute(
        "UPDATE farms SET total = $1 WHERE user_id = $2", total, user_id
    )


async def get_total(user_id: int):
    return await db_connection.pool.fetchval(
        "SELECT total FROM farms WHERE user_id = $1", user_id
    )


async def get_last_date(user_id: int):
    return await db_connection.pool.fetchval(
        "SELECT created_date FROM farms WHERE user_id = $1", user_id
    )
