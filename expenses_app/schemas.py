from pydantic import BaseModel


class ExpenseSchema(BaseModel):
    name: str


class CategoriesSchema(BaseModel):
    name: str
