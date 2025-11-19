"""
Обработчик команды /help.

Ты можешь создавать здесь документацию или подсказки.
"""

from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help_handler(msg: types.Message):
    await msg.answer("Список команд:\n/start — запуск бота\n/help — помощь")
