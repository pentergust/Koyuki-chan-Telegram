from aiogram import Dispatcher, types

from routers.main_menu import (
    get_welcome_text,  # Импортируем функцию кэширования
)


async def handle_back_to_menu(call: types.CallbackQuery):
    text = await get_welcome_text()  # Используем кэшированную функцию
    
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📚 Список дз", callback_data="homework_list")],
        [types.InlineKeyboardButton(text="🎥 Записи вебинара", callback_data="webinar_records")],
        [types.InlineKeyboardButton(text="❓ Помощь", callback_data="help")],
        [types.InlineKeyboardButton(text="ℹ️ Информация о боте", callback_data="bot_info")]
    ])
    
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown')

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(handle_back_to_menu, lambda call: call.data == "back_to_menu")
