from aiogram import Bot, Dispatcher
from expenses_app.settings import TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN)

dp = Dispatcher(bot)
# dp.setup_webhook