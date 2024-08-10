from aiocache import cached
from aiogram import Dispatcher, types


@cached(ttl=300)
async def get_homework_list_text():
    return """
    **ДОМАШНИЕ ЗАДАНИЯ ТРЕТЬЕГО МОДУЛЯ**

    *1 вебинар*. Тема: Знакомство с телеграмм ботами, получение токена, создание первой команды 
    ➡️ **Домашнее задание**: [ссылка](https://telegra.ph/Domashnee-zadanie-1-07-23)
    **Дедлайн**: до 15.07

    *2 вебинар*. Тема: Обработка команд пользователя, работа с текстовыми сообщениями 
    ➡️ **Домашнее задание**: [ссылка](https://telegra.ph/Domashnee-zadanie-2-07-23)
    **Дедлайн**: до 17.07

    *3 вебинар*. Тема: Работа с файловой системой, чтение и запись файлов, отправка файлов ботом 
    ➡️ **Домашнее задание**: [ссылка](https://telegra.ph/Domashnee-zadanie-3-07-23)
    **Дедлайн**: до 19.07

    *4 вебинар*. Тема: JSON. Работа с публичными API, отправка случайного изображения, библиотека requests 
    ➡️ **Домашнее задание**: [ссылка](https://telegra.ph/Domashnee-zadanie-4-07-23-2)
    **Дедлайн**: до 23.07

    *6 вебинар*. Тема: Кнопки в боте 
    ➡️ **Домашнее задание**: [ссылка](https://telegra.ph/Domashnee-zadanie-6-07-23)
    **Дедлайн**: до 25.07

    *9 вебинар*. Тема: Телеграмм бот с 1-ой игрой 
    ➡️ **Домашнее задание**: [ссылка](https://telegra.ph/Domashnee-zadanie-9-Itogovyj-proekt-07-23)
    **Дедлайн**: до 30.07

    *P/S* Можно открыть и решить, как только найдется свободная минутка (работает даже тогда, когда не работает ЛМС)

    **Важно**: для перевода на следующий модуль обязательное количество домашних заданий - 3 штуки, сданный тест и одно посещение вебинара.
    """


async def handle_homework_list(call: types.CallbackQuery):
    text = await get_homework_list_text()
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Назад в меню", callback_data="back_to_menu"
                )
            ]
        ]
    )
    await call.message.edit_text(
        text,
        reply_markup=markup,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )


def register_handlers(dp: Dispatcher):
    dp.callback_query.register(
        handle_homework_list, lambda call: call.data == "homework_list"
    )
