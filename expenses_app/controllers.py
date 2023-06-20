from .database import engine, get_connection
from .models import CategoryModel
from . import logger
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker


@logger.log_this_output
async def get_categories() -> dict:
    async with engine.connect() as conn:
        results = await conn.execute(select(CategoryModel))
    serialized = {k: v for k, v in results.all()}
    return serialized


@logger.log_this_input_and_output
async def add_category(data: dict):
    new_category = CategoryModel(**data)
    async with get_connection() as conn:
        conn.add(new_category)
        await conn.commit()
        await conn.refresh(new_category)
    return new_category
