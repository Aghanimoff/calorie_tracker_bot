from aiogram import Bot, Dispatcher, executor, types
from .config import API_TOKEN
from .handlers import register_handlers

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

if __name__ == "__main__":
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
