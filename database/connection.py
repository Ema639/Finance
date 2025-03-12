from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine("postgresql+asyncpg://postgres:password@localhost:5432/database")

AsyncSession = async_sessionmaker(engine, expire_on_commit=False)
