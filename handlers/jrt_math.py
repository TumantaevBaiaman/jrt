from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="YOUR_TOKEN")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Отправляем изображение
    with open("image.jpg", "rb") as photo:
        await message.reply_photo(photo, caption="Описание изображения")

    # Создаем объект InlineKeyboardMarkup с вариантами ответов
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Вариант 1", callback_data="option1"))
    keyboard.add(types.InlineKeyboardButton(text="Вариант 2", callback_data="option2"))
    keyboard.add(types.InlineKeyboardButton(text="Вариант 3", callback_data="option3"))

    # Создаем объект Poll
    poll = types.Poll(
        type=types.PollType.REGULAR,
        question="Вопрос опроса",
        options=["Вариант 1", "Вариант 2", "Вариант 3"],
        is_anonymous=True,
        allows_multiple_answers=False,
        correct_option_id=0  # Индекс правильного варианта ответа
    )

    # Отправляем опрос с клавиатурой
    await message.reply_poll(poll=poll, reply_markup=keyboard)