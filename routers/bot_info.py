"""Информация о боте.

Данный обработчик немного раскажет, что это за бот и для чего его
можно будет использовать.

Предоставляет
-------------

- bot_info: Информация о боте
"""

from aiogram import Dispatcher, F, Router
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

router = Router(name=__name__)


# Компоненты сообщений
# ====================

BOT_INFO = (
    "*О Koyuki-chan*\n\n"
    "Привет! Я Koyuki-chan, ваша виртуальная помощница.\n"
    "Я создана для упрощения навигации по курсу Python.\n"
    "Моя миссия — помочь Вам *легко и удобно* получать доступ к информации"
    " по курсу и домашним заданиям.\n\n"

    "*Мои возможности:*\n"
    "- 📚 **Список домашних заданий** и их дедлайны.\n"
    "- 🎥 **Записи вебинаров**: Никогда не пропустите важный вебинар.\n"
    "- ❓ **Помощь по курсу**: Я помогу найти нужную информацию.\n\n"

    "*О проекте:*\n"
    "- Разработка и поддержка осуществляется на чистом энтузиазме.\n"
    "- Буду очень рада, если вы внесёте свой вклад.\n\n"

    "*Исходный код:*\n"
    "- Вы можете найти на [github]"
    "(https://github.com/chimichubanga/Koyuki-chan-TelegramBOT)\n"
    "- *Автор*: [@chimichubanga](https://t.me/chimichubanga)\n"
    "- Не стесняйтесь писать автору, если есть идеи/замечания.\n\n"

    "Списибо что используете Koyuki-chan! Успехов в изучении Python!"
)

TO_HOME_MARKUP = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")
]])


# Обработчики
# ===========

@router.callback_query(F.data=="bot_info")
async def handle_bot_info(query: CallbackQuery):
    """Информация о боте.

    Данный раздел предоставляет основную информацию о боте.
    Описание, возможности бота, автор, как помочь проекту.
    """
    await query.message.edit_text(BOT_INFO, reply_markup=TO_HOME_MARKUP)


# Загрузка обработчика
# ====================

def register_handlers(dp: Dispatcher) -> None:
    """Загрузчик обработчика.

    Данная функция вызывается при запуске бота.
    Она добавляет роутер к диспетчеру.
    Это позволяет использовать определённые в роутере обработчики
    диспетчером.
    """
    dp.include_router(router)
