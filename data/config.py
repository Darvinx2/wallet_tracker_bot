import os

import dotenv

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MORALIS_API_TOKEN = os.getenv("MORALIS_API_TOKEN")

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set")

if not MORALIS_API_TOKEN:
    raise ValueError("MORALIS_API_TOKEN environment variable is not set")
