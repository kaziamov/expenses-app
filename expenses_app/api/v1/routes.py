from fastapi import APIRouter

from expenses_app.schemas import ExpenseSchema, CategoriesSchema
from expenses_app import controllers


router = APIRouter()


@router.get("/expenses")
async def get_expenses():
    return await controllers.get_expenses()


@router.post("/expenses/create")
async def create_expense(item: ExpenseSchema):
    data = dict(item)
    return await controllers.add_expense(data)


@router.patch("/expenses/{exp_id}/edit")
async def edit_expense(exp_id: str):
    return


@router.delete("/expenses/{exp_id}/delete")
async def delete_expense(exp_id: str):
    return await controllers.delete_expense(exp_id)


@router.get("/categories")
async def get_categories():
    return await controllers.get_categories()


@router.post("/categories/create")
async def create_category():
    return await controllers.get_categories()


@router.patch("/categories/{exp_id}/edit")
async def edit_category(exp_id: str):
    return await controllers.edit_category(exp_id)
