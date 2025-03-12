from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, Enum, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = 'User'  # TODO назавание на англ

    name = Column(String(), nullable=False)
    email = Column(String(), unique=True, nullable=False)
    password_hash = Column(String(), nullable=False)
    registration_date = Column(TIMESTAMP, default=func.now())

    categories = relationship('Category', back_populates='user', cascade="all, delete")
    transactions = relationship('Transaction', back_populates='user', cascade="all, delete")


class Category(Base):
    __tablename__ = 'Category'  # TODO назавание на англ

    name = Column(String(), nullable=False)
    type = Column(Enum('доход', 'расход', name='transactiontype'), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('User.id', ondelete="CASCADE"), nullable=False)

    user = relationship('User', back_populates='categories')
    transactions = relationship('Transaction', back_populates='category')


class Transaction(Base):
    __tablename__ = 'Transaction'  # TODO назавание на англ

    user_id = Column(Integer, ForeignKey('User.id', ondelete="CASCADE"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    type = Column(Enum('доход', 'расход', name='transactiontype'), nullable=False)
    date = Column(TIMESTAMP, default=func.now())
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('Category.id', ondelete="SET NULL"))

    user = relationship('User', back_populates='transactions')
    category = relationship('Category', back_populates='transactions')
