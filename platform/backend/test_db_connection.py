import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

async def test_db():
    try:
        print(f"Connecting to {DATABASE_URL}...")
        engine = create_async_engine(DATABASE_URL)
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_db())
