
from create_bot import dp
from aiogram.utils import executor
from handlers import commands, jrt_math, jrt_math2, jrt_analogia, jrt_grammar, user, gpt

commands.register_admin(dp)
jrt_math.register_quiz(dp)
jrt_math2.register_quiz2(dp)
jrt_analogia.register_quiz_analogia(dp)
jrt_grammar.register_quiz_grammar(dp)
user.register_quiz_eng(dp)
gpt.register_gpt(dp)
executor.start_polling(dp, skip_updates=True)