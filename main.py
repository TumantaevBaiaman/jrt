# Импортируем объект dp из модуля bot
from bot import dp

# Импортируем функцию executor из модуля aiogram.utils
from aiogram.utils import executor

# Импортируем модули с обработчиками событий
from handlers import jrt_math

# Регистрируем обработчик симпатичных животных
logic_cute_animals.register_cute_animals(dp)

# Регистрируем обработчик викторин
logic_quiz.register_quiz(dp)

# Запускаем бесконечный цикл опроса бота
# skip_updates=True говорит боту пропускать необработанные обновления, если такие есть
executor.start_polling(dp, skip_updates=True)