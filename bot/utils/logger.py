"""
Настройки логов с помощью loguru.
"""

from loguru import logger

# Пример форматирования логов
logger.add("logs.log", format="{time} {level} {message}", level="INFO")

# Использование:
# logger.info("Бот запущен")
