"""Корневые настройки бота.

Данные настройки будут загружены вместе с загрузкой бота.

большинство из них задано через .env файл.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# Токен Telegram API для рабоыт бота
TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

# Если пользователь не указал токен, то дальше нам делать нечего
# так что любзено попросим его укзаать токен в переменные окружения
if TOKEN is None:
    raise ValueError("Please enter your bot token in enviroment variables")

# Когда данное значение True, после запуска бот автоматически настроит
# свой спиоск команд
# как если бы вы настраивали его самостоятельно через Bot father
# Рекомендауется включить один раз при первом запуске, а плсле отключить.
SET_COMMANDS = False
