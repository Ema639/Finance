from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

# Подключение к БД
engine = create_async_engine("postgresql+asyncpg://postgres:password@localhost:5432/database")

# Создание асинхронной сессии
AsyncSession = async_sessionmaker(engine, expire_on_commit=False)
