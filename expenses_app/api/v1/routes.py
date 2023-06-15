from fastapi import APIRouter
from .controllers import get_expenses, add_expense, edit_expense
from .schemas import ExpenseSchema


router = APIRouter()


@router.get("/expenses")
async def expenses():
    return await get_expenses()


@router.post("/expenses/create")
async def expense_create(item: ExpenseSchema):
    data = dict(item)
    return await add_expense(data)


@router.patch("/expenses/{exp_id}/edit")
async def expense_edit(exp_id: str):
    return


@router.put("/expenses/{exp_id}/edit")
async def expense_delete(exp_id: str):
    return await edit_expense(exp_id)
