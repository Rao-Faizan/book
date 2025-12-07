import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text, inspect

DATABASE_URL = "sqlite+aiosqlite:///./textbook_platform.db"

async def check_tables():
    engine = create_async_engine(DATABASE_URL)
    async with engine.connect() as conn:
        tables = await conn.run_sync(lambda sync_conn: inspect(sync_conn).get_table_names())
        print(f"Tables found: {tables}")

if __name__ == "__main__":
    asyncio.run(check_tables())
