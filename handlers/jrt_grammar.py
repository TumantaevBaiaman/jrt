import asyncio

from aiogram.dispatcher import FSMContext

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
# from key.buttons import main_menu
from data import jrt


class FSMChatGPTGrammar(StatesGroup):
    poll = State()
    question = 0
    ls = 0
    result = 0


async def cm_start_grammar(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ls'] = 0
        data['result'] = 0

    await show_poll_grammar(message, state)


async def show_poll_grammar(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        ls = data['ls']

    if ls < len(jrt.jrt_math_strange_2):
        text = jrt.jrt_grammar[ls][0]
        options = jrt.jrt_grammar[ls][1]

        poll_options = []
        for i, option in enumerate(options):
            button = types.InlineKeyboardButton(text=option, callback_data=f'answer_{i}')
            poll_options.append([button])

        reply_markup = types.InlineKeyboardMarkup(inline_keyboard=poll_options)

        await bot.send_message(message.from_user.id, text, reply_markup=reply_markup)

        async with state.proxy() as data:
            data['ls'] += 1

        await FSMChatGPTGrammar.poll.set()

    else:
        async with state.proxy() as data:
            result = data['result']
        await bot.send_message(message.from_user.id, f"Жыйынтык:\n{result} туура\n{10-result} ката жооп")
        await state.finish()


async def process_poll_answer_grammar(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        ls = data['ls']-1
        correct_answer = jrt.jrt_grammar[ls][-1]
        if str(correct_answer) == callback_query.data.replace("answer_", ""):
            data['result'] += 1
    await show_poll_grammar(callback_query, state)


def register_quiz_grammar(dp: Dispatcher):
    dp.register_message_handler(cm_start_grammar, Text(equals='📝 Грамматика', ignore_case=True))
    dp.register_callback_query_handler(process_poll_answer_grammar, state=FSMChatGPTGrammar.poll)