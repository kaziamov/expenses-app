from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class BaseDBModel(DeclarativeBase):
    """Basic class for all DB models"""
    id = Column(Integer, primary_key=True, autoincrement=True)


class AccountModel(BaseDBModel):
    """Model for Money Accounts"""
    __tablename__ = "accounts"

    name = Column(String, nullable=False, unique=True)


class CategoryModel(BaseDBModel):
    """Model for Category"""
    __tablename__ = "categories"

    name = Column(String, nullable=False, unique=True)


class ExpenseModel(BaseDBModel):
    """Model for Expenses"""
    __tablename__ = "expenses"

    name = Column(String, nullable=True)
    accounts_id = Column(Integer, ForeignKey("accounts.id"))
    category = relationship("CategoryModel", backref="expenses")
    category_id = Column(Integer, ForeignKey("categories.id"))
    account = relationship("AccountModel", backref="expenses")
