from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot

from .settings import WEBHOOK_PATH, WEBHOOK_URL
from .api.v1.routes import router
from .bot.app import dp, bot

app = FastAPI()
app.include_router(router, prefix="")


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()


# TODO: remove after
@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
