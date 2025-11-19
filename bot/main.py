"""
Главная точка входа в приложение.

Здесь запускается бот:
- подключаются роутеры
- запускается polling
"""

import asyncio
from aiogram import Dispatcher
from loader import bot, dp

# Импортируй здесь свои обработчики
from handlers.start import router as start_router


async def main():
    """
    Основная асинхронная функция.
    Всё приложение стартует отсюда.
    """

    # Подключаем роутеры
    dp.include_router(start_router)

    # Запуск long polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
