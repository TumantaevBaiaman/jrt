import aiohttp
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from bot import dp, bot
from key import buttons


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Салам мен сага ЖРТга даярданууга жардам берем', reply_markup=buttons.main_menu_m)


async def jrt_m(message: types.Message):
    await bot.send_message(message.from_user.id, 'ЖРТ болуму', reply_markup=buttons.main_menu)


async def math_m(message: types.Message):
    await bot.send_message(message.from_user.id, 'Математика болуму', reply_markup=buttons.main_menu_math)


async def back_m(message: types.Message):
    await bot.send_message(message.from_user.id, 'Артка', reply_markup=buttons.main_menu)


async def back_m2(message: types.Message):
    await bot.send_message(message.from_user.id, 'Артка', reply_markup=buttons.main_menu_m)


def register_admin(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(jrt_m, Text(equals='✔️ЖРТ', ignore_case=True))
    dp.register_message_handler(math_m, Text(equals='🧮 Математика', ignore_case=True))
    dp.register_message_handler(back_m, Text(equals='◀️Артка', ignore_case=True))
    dp.register_message_handler(back_m2, Text(equals='⬅️Артка', ignore_case=True))