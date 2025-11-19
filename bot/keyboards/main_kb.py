"""
Здесь создаются кнопки (ReplyKeyboardMarkup, InlineKeyboardMarkup).

Используй этот файл как шаблон.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    """
    Возвращает основную клавиатуру.
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Меню")],
        ],
        resize_keyboard=True
    )
    return kb
