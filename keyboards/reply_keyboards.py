from utils.dict import *
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

greeting_keys = (KeyboardButton(text=word) for word in keyboard_words)
greeting_keyboard = ReplyKeyboardMarkup(
    keyboard=[[next(greeting_keys) for _ in range(2)] for _ in range(3)],
    resize_keyboard=True,
    one_time_keyboard=False
)
