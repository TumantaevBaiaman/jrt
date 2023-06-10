
import asyncio
import openai

from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from key.buttons import main_menu, main_menu_stop

import settings_openai


class FSMChatGPT(StatesGroup):
    question = State()


async def cm_start_gpt(message: types.Message):
    await bot.send_message(message.from_user.id, 'Задайте свой вопрос')
    await FSMChatGPT.question.set()


async def question_gpt(message: types.Message, state: FSMChatGPT):
    text = message.text
    user_id = message.from_user.id

    print(text)
    if text == "❌токто":
        await state.finish()
        await bot.send_message(user_id, "😊Жардам бергениме кубанычтамын.", reply_markup=main_menu)

    else:
        await bot.send_message(user_id, "⏳ ...")

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt="Маанисин чечмеле кыргызча "+text,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.0
        )

        generated_text = response.choices[0].text.strip()

        await bot.send_message(user_id, generated_text, reply_markup=main_menu_stop)


def register_gpt(dp : Dispatcher):
    dp.register_message_handler(cm_start_gpt, Text(equals='🧐 Маанисин табу', ignore_case=True))
    dp.register_message_handler(question_gpt, state=FSMChatGPT.question)