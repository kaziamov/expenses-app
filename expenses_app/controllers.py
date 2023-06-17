from .database import engine, get_connection
from .models import CategoryModel
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker


async def get_categories() -> dict:
    async with engine.connect() as conn:
        results = await conn.execute(select(CategoryModel))
    return {k: v for k, v in results.all()}


async def add_category(data: dict):
    new_category = CategoryModel(**data)
    async with get_connection() as conn:
        conn.add(new_category)
        await conn.commit()
        await conn.refresh(new_category)
    return new_category

