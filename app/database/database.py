import os
from dotenv import load_dotenv
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# 환경 변수 로드
load_dotenv()   

database_url = os.getenv("DATABASE_ENDPOINT")

metadata = MetaData()

engine = create_async_engine(
    database_url,
    echo=False,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True
)

async_session = async_sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
)

async def get_db() -> AsyncSession:
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
