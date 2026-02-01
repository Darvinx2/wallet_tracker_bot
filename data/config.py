import os

import dotenv

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MORALIS_API_TOKEN = os.getenv("MORALIS_API_TOKEN")

DB_CONNECT = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST"),
}

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

if not MORALIS_API_TOKEN:
    raise ValueError("MORALIS_API_TOKEN environment variable is not set")

if not DB_CONNECT["password"]:
    raise ValueError("DB_PASSWORD environment variable is not set")
