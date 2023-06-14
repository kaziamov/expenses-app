from fastapi import FastAPI
from .v1.routes import router as v1_routes

app = FastAPI()
app.include_router(v1_routes, prefix="/api/v1")

@app.get('/')
async def root():
    return {"Hello":"World"}
