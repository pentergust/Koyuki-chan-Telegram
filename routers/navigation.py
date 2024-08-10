"""Возврат в главное меню.

Проедоставляет вохможность вернуться в главное меню, по нажатию на
кнопку.

Предоставляет
-------------

- back_to_menu: Вернуться в главное меню.
"""

from aiogram import Dispatcher, types

from routers.main_menu import (
    get_welcome_text,  # Импортируем функцию кэширования
)

# Обработчики
# ===========

async def handle_back_to_menu(call: types.CallbackQuery):
    text = await get_welcome_text()  # Используем кэшированную функцию

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

    await call.message.edit_text(
        text, reply_markup=markup, parse_mode="Markdown"
    )


# загрузка роутера
# ================

def register_handlers(dp: Dispatcher):
    """Загрузчик обработчика.

    Данная функция вызывается при запуске бота.
    Она добавляет роутер к диспетчеру.
    Это позволяет использовать определённые в роутере обработчики
    диспетчером.
    """
    dp.callback_query.register(
        handle_back_to_menu, lambda call: call.data == "back_to_menu"
    )
