from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

# хэндлер для текстовых сообщений, которые не попали в другие хэндлеры
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])

# функция для регистрации хэндлера Вызыаемая в основном модуле bot.py
def register_other_hadler(dp: Dispatcher):
    dp.register_message_handler(send_answer)