from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Handling for SQLite vs Postgres
connect_args = {}
if "sqlite" in settings.DATABASE_URL:
    connect_args = {"check_same_thread": False}

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args=connect_args
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
