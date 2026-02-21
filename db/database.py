from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from data.config import DATABASE_URL


url = DATABASE_URL

engine = create_async_engine(
    url=url,
    echo=True,
)

session = async_sessionmaker(
    bind=engine,
    autoflush=True,
    expire_on_commit=False,
)
