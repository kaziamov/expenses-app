from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.v1.routes import router as v1_routes

app = FastAPI()
app.include_router(v1_routes, prefix="/api/v1")


# TODO: remove after
@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
