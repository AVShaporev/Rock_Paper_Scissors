from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from lexicon.lexicon_ru import LEXICON_RU


# содание клавиатуры с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                     resize_keyboard=True)
button_yes: KeyboardButton = KeyboardButton('Давай!')
button_no: KeyboardButton = KeyboardButton('Не хочу!')

# распрложеие кнопок рядом друг с другом
yes_no_kb.add(button_yes, button_no)

# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)

button_1: KeyboardButton = KeyboardButton('rock')
button_2: KeyboardButton = KeyboardButton('scissors')
button_3: KeyboardButton = KeyboardButton('paper')

# Располагаем кнопки в клавиатуре одну под другой в 3 ряда
game_kb.add(button_1).add(button_2).add(button_3)