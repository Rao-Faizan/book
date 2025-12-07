import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.db import Base
from app.models.user import UserProfile
from app.core.config import settings

async def init_db():
    print(f"Connecting to {settings.DATABASE_URL}...")
    engine = create_async_engine(settings.DATABASE_URL)
    
    async with engine.begin() as conn:
        print("Creating tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created.")
        
    print("Verification:")
    async with engine.connect() as conn:
        from sqlalchemy import inspect, text
        tables = await conn.run_sync(lambda sync_conn: inspect(sync_conn).get_table_names())
        print(f"Tables: {tables}")

if __name__ == "__main__":
    asyncio.run(init_db())
