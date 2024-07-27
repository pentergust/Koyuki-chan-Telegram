"""Главный файл бота.

настраивает все компоненты бота.
подключает внешние обработчики.
Запускает обработчик событий.
"""

import asyncio
import logging

from aiocache import caches
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, Update

from loguru import logger

from cogs import (
    bot_info,
    bot_help,
    homework_help,
    homework_list,
    main_menu,
    navigation,
    webinar_records,
)
import config

# Глобальные переменные
# =====================

# Инициализация диспетчера с использованием памяти для хранения состояний
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Глобальный список всех комад бота
# Используется чтобы автоматически настраивать список команд в Telegram
COMMANDS = [
    BotCommand(command="/start", description="Запустить бота"),
    BotCommand(command="/menu", description="Показать меню")
]

# Список всех обработчиков бота.
# После он будет перенесён в другое место.
ROUTERS = [
    bot_info,
    bot_help,
    homework_help,
    homework_list,
    main_menu,
    navigation,
    webinar_records
]


# Обработчики бота
# ================

@dp.errors()
async def on_error(update: Update, exception: Exception):
    """Глобальный обарботчик ошибок.

    Как только что-то в боте пойдёт не так, этот обработчик тут же
    поймает это и обработает внутри себя.
    """
    loguru.error("Update {} caused {}", update, exception)
    if isinstance(update, types.CallbackQuery):
        await update.message.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")
    elif isinstance(update, types.Message):
        await update.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")
    return True


# Функция запуска бота
# ====================

async def main():
    """Производит настройку и запуск компонентов бота.

    Настраивает обработчики, логгирование, кэширование.
    """
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler()
        ]
    )

    # Настройка кэширования
    caches.set_config({
        'default': {
            'cache': 'aiocache.SimpleMemoryCache',
            'serializer': {
                'class': 'aiocache.serializers.PickleSerializer'
            }
        }
    })

    logger.info("Load routers")
    for router in ROUTERS:
        router.register_handlers(dp)
    logger.success("Load routers complete")

    # Инициализация бота
    bot = Bot(token=config.TOKEN)

    if config.SET_COMMANDS:
        logger.info("Update bot commands")
        await bot.set_my_commands(COMMANDS)
    await dp.start_polling(bot)


# Запуск скрипта
# ==============

if __name__ == '__main__':
    asyncio.run(main())
