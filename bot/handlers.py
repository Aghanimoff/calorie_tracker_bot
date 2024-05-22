from aiogram import Dispatcher, types
from .api_integration import analyze_user_input

async def start_command(message: types.Message):
    await message.reply("Привет! Пожалуйста, введи информацию о своём рационе и физической активности за вчера.")

async def analyze_input(message: types.Message):
    response = await analyze_user_input(message.text)  # Добавлен await для асинхронной функции
    await message.reply(response)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(analyze_input, content_types=["text"])
