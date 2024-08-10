"""Главно меню.

Осуществляет навигацию по всем основным разделам бота.

Предоставляет
-------------

- /start /menu (back_to_menu): Главнао меню.
"""

from aiocache import cached
from aiogram import Dispatcher, types, Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from aiogram.filters import Command

router = Router(name=__name__)

# Компоненты сообщений
# ====================

WELCOME_TEXT = (
    "*Добро пожаловать главное меню Koyuki-chan!*"
    "Я ваша виртуальная помощница, созданная для упрощения навигации по курсу"
    " \"Код будущего\"."
)

MAIN_MENU_MARKUP = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="📚 Список дз", callback_data="homework_list"),
    InlineKeyboardButton
        (text="🎥 Записи вебинара", callback_data="webinar_records"
    ),
    InlineKeyboardButton(text="❓ Помощь", callback_data="help"),
    InlineKeyboardButton(text="ℹ️ Информация о боте", callback_data="bot_info")
]])


# Обработчики
# ===========

@router.message(Command("start"))
@router.message(Command("menu"))
async def main_menu_command(message: Message):
    await message.answer(WELCOME_TEXT, reply_markup=MAIN_MENU_MARKUP)

@router.callback_query(F.data == "back_to_menu")
async def main_menu_callback(query: CallbackQuery):
    await query.message.answer(WELCOME_TEXT, reply_markup=MAIN_MENU_MARKUP)


# Загрузки роутера
# ================

def register_handlers(dp: Dispatcher):
    """Загрузчик обработчика.

    Данная функция вызывается при запуске бота.
    Она добавляет роутер к диспетчеру.
    Это позволяет использовать определённые в роутере обработчики
    диспетчером.
    """
    dp.include_router(router)
