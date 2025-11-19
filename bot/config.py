"""
Модуль конфигурации.

Содержит:
- dataclass Config
- загрузку переменных окружения из .env
"""

from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Загружаем переменные из .env файла
load_dotenv()

@dataclass
class Config:
    """
    Главный объект конфигурации приложения.
    Хранит токен, список админов и любые другие настройки.
    """
    bot_token: str
    admins: list[int]


def get_config():
    """
    Читает данные из .env файла и возвращает объект Config.
    """
    return Config(
        bot_token=os.getenv("BOT_TOKEN"),
        admins=list(map(int, os.getenv("ADMINS", "").split()))
    )
