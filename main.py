import asyncio
import logging

from aiocache import caches
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from cogs import (
    bot_info,
    help,
    homework_help,
    homework_list,
    main_menu,
    navigation,
    webinar_records,
)
from config import TOKEN

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

# Инициализация бота
bot = Bot(token=TOKEN)
# Инициализация диспетчера с использованием памяти для хранения состояний
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация обработчиков
main_menu.register_handlers(dp)
navigation.register_handlers(dp)
homework_list.register_handlers(dp)
webinar_records.register_handlers(dp)
bot_info.register_handlers(dp)
help.register_handlers(dp)
homework_help.register_handlers(dp)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/menu", description="Показать меню")
    ]
    await bot.set_my_commands(commands)

# Глобальный обработчик ошибок
async def on_error(update: types.Update, exception: Exception):
    logging.error(f"Update {update} caused error {exception}")
    if isinstance(update, types.CallbackQuery):
        await update.message.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")
    elif isinstance(update, types.Message):
        await update.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")
    return True

dp.errors.register(on_error)

async def main():
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
