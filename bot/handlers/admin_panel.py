"""
Обработчики администраторов.
Здесь логика:
- админ меню
- статистика
- управление пользователями
"""

from aiogram import Router, types

router = Router()


@router.message()
async def admin_menu(msg: types.Message):
    # Здесь ты проверишь id пользователя, прежде чем выполнять код
    await msg.answer("Админ-панель ещё пустая.")
