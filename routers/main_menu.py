"""Главно меню.

Осуществляет навигацию по всем основным разделам бота.

Предоставляет
-------------

- /start /menu: Главнао меню.
"""

from aiocache import cached
from aiogram import Dispatcher, types
from aiogram.filters import Command

# Компоненты сообщений
# ====================

@cached(ttl=60)
async def get_welcome_text():
    return """
    **Добро пожаловать в Koyuki-chan!**

    Я Koyuki-chan, ваша виртуальная помощница, созданная для упрощения навигации по курсу "Код будущего".
    """


# Обработчики
# ===========

async def send_welcome(message: types.Message):
    text = await get_welcome_text()

    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="📚 Список дз", callback_data="homework_list"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="🎥 Записи вебинара", callback_data="webinar_records"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="❓ Помощь", callback_data="help"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="ℹ️ Информация о боте", callback_data="bot_info"
                )
            ],
        ]
    )

    await message.answer(text, reply_markup=markup, parse_mode="Markdown")


# Загрузки роутера
# ================

def register_handlers(dp: Dispatcher):
    """Загрузчик обработчика.

    Данная функция вызывается при запуске бота.
    Она добавляет роутер к диспетчеру.
    Это позволяет использовать определённые в роутере обработчики
    диспетчером.
    """
    dp.message.register(send_welcome, Command("start"))
    dp.message.register(send_welcome, Command("menu"))
