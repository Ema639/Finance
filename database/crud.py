from sqlalchemy.future import select
from models import User, Category, Transaction
from connection import AsyncSession


# CRUD операции для Пользователя
async def create_user(name, email, password_hash):
    async with AsyncSession() as session:
        new_user = User(name=name, email=email, password_hash=password_hash)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


async def get_user_by_id(user_id: int) -> User | None:
    async with AsyncSession() as session:
        result = await session.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()


async def get_all_users():
    async with AsyncSession() as session:
        result = await session.execute(select(User))
        return result.scalars().all()


async def update_user(user_id: int, name=None, email=None, password_hash=None):
    async with AsyncSession() as session:
        result = await session.execute(select(User).filter(User.id == user_id))
        user_to_update = result.scalars().first()
        if user_to_update:
            if name:
                user_to_update.name = name
            if email:
                user_to_update.email = email
            if password_hash:
                user_to_update.password_hash = password_hash
            await session.commit()
        return user_to_update


async def delete_user(user_id: int):
    async with AsyncSession() as session:
        result = await session.execute(select(User).filter(User.id == user_id))
        user_to_delete = result.scalars().first()
        if user_to_delete:
            await session.delete(user_to_delete)
            await session.commit()
            return True
        return False


# CRUD операции для Категории
async def create_category(name, category_type, user_id, description=None):
    async with AsyncSession() as session:
        new_category = Category(name=name, type=category_type, user_id=user_id, description=description)
        session.add(new_category)
        await session.commit()
        await session.refresh(new_category)
        return new_category


async def get_category_by_id(category_id: int):
    async with AsyncSession() as session:
        result = await session.execute(select(Category).filter(Category.id == category_id))
        return result.scalars().first()


async def get_categories_by_user(user_id: int):
    async with AsyncSession() as session:
        result = await session.execute(select(Category).filter(Category.user_id == user_id))
        return result.scalars().all()


async def update_category(category_id: int, name=None, category_type=None, description=None):
    async with AsyncSession() as session:
        result = await session.execute(select(Category).filter(Category.id == category_id))
        category_to_update = result.scalars().first()
        if category_to_update:
            if name:
                category_to_update.name = name
            if category_type:
                category_to_update.type = category_type
            if description:
                category_to_update.description = description
            await session.commit()
        return category_to_update


async def delete_category(category_id: int):
    async with AsyncSession() as session:
        result = await session.execute(select(Category).filter(Category.id == category_id))
        category_to_delete = result.scalars().first()
        if category_to_delete:
            await session.delete(category_to_delete)
            await session.commit()
            return True
        return False


# CRUD операции для Транзакции
async def create_transaction(user_id, amount, transaction_type, category_id=None, description=None):
    async with AsyncSession() as session:
        new_transaction = Transaction(
            user_id=user_id,
            amount=amount,
            type=transaction_type,
            category_id=category_id,
            description=description
        )
        session.add(new_transaction)
        await session.commit()
        await session.refresh(new_transaction)
        return new_transaction


async def get_transaction_by_id(transaction_id: int):
    async with AsyncSession() as session:
        result = await session.execute(select(Transaction).filter(Transaction.id == transaction_id))
        return result.scalars().first()


async def get_transactions_by_user(user_id: int):
    async with AsyncSession() as session:
        result = await session.execute(select(Transaction).filter(Transaction.user_id == user_id))
        return result.scalars().all()


async def update_transaction(
        transaction_id: int, amount=None, transaction_type=None, category_id=None,
        description=None):
    async with AsyncSession() as session:
        result = await session.execute(select(Transaction).filter(Transaction.id == transaction_id))
        transaction_to_update = result.scalars().first()
        if transaction_to_update:
            if amount:
                transaction_to_update.amount = amount
            if transaction_type:
                transaction_to_update.type = transaction_type
            if category_id:
                transaction_to_update.category_id = category_id
            if description:
                transaction_to_update.description = description
            await session.commit()
        return transaction_to_update


async def delete_transaction(transaction_id: int):
    async with AsyncSession() as session:
        result = await session.execute(select(Transaction).filter(Transaction.id == transaction_id))
        transaction_to_delete = result.scalars().first()
        if transaction_to_delete:
            await session.delete(transaction_to_delete)
            await session.commit()
            return True
        return False
