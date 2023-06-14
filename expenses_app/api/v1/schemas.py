from pydantic import BaseModel

class ExpenseSchema(BaseModel):
    name: str