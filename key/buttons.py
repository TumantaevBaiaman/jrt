from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton

g1 = KeyboardButton('✔️Английский')
g2 = KeyboardButton('✔️ЖРТ')

b1 = KeyboardButton('🎏 Аналогия')
b2 = KeyboardButton('📝 Грамматика')
b3 = KeyboardButton('🧮 Математика')
# b4 = KeyboardButton('🧐 Маанисин табу')
b5 = KeyboardButton('⬅️Артка')

m1 = KeyboardButton('📐 1-бөлум')
m2 = KeyboardButton('📏 2-бөлум')
m3 = KeyboardButton('◀️Артка')

s = KeyboardButton('❌токто')

main_menu_m = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_m.add(g1, g2)


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(b1, b2, b3).add(b5)

main_menu_math = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_math.add(m1, m2).add(m3)

main_menu_stop = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_stop.add(s)