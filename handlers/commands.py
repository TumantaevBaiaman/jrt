import aiohttp
from aiogram import types, Dispatcher
from bot import dp, bot


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Я умный бот, готовый помочь вам в чем-то. Чем я могу быть полезен?')


def register_admin(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])