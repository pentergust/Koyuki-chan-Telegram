"""Список вебинаров.

Предоставляет список всех вебинаров, время их проведения и ссылки
на записи вебинаров.

Предоставляет
-------------

- webinar_records: Список вебинаров
"""

from aiocache import cached
from aiogram import Dispatcher, types

# Компоненты сообщений
# ====================

@cached(ttl=300)
async def get_webinar_records_text():
    return """
    **ЗАПИСИ ВЕБИНАРОВ ТРЕТЬЕГО МОДУЛЯ**

    *1 вебинар*. Тема: Знакомство с телеграмм ботами, получение токена, создание первой команды
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240710_znakomstvo_s_tg_botami_16_00_mishin.mp4)

    *2 вебинар*. Тема: Обработка команд пользователя, работа с текстовыми сообщениями
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240713_obrabotka_komand_16_00_mishin.mp4)

    *3 вебинар*. Тема: Работа с файловой системой, чтение и запись файлов, отправка файлов ботом
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240715_rabota_s_faylov_mishin_16_00.mp4)

    *4 вебинар*. Тема: JSON. Работа с публичными API, отправка случайного изображения, библиотека requests
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240719_json_rabota_s_p_mishin_16_00.mp4)

    *5 вебинар*. Тема: Бот отправляющий текущий прогноз погоды
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240721_bot_otpravl_prognoz_pog_16_00_mish.mp4)

    *6 вебинар*. Тема: Кнопки в боте
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240726_knopki_v_bote_16_00_mish.mp4)

    *7 вебинар*. Тема:  Игра в чат-боте
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240727_igra_v_chat_bot_mishin_16_00.mp4)

    *8 вебинар*. Тема:  Игра в чат-боте часть 2
    (Время проведения : 29.07 16:00-17:40)
    по ссылке: [ссылка](https://my.mts-link.ru/j/3080305/413797792)
    """


# Обработчики
# ===========

async def handle_webinar_records(call: types.CallbackQuery):
    text = await get_webinar_records_text()
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="⬅️ Назад в меню", callback_data="back_to_menu"
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


# Загрузка роутера
# ================

def register_handlers(dp: Dispatcher):
    """Загрузчик обработчика.

    Данная функция вызывается при запуске бота.
    Она добавляет роутер к диспетчеру.
    Это позволяет использовать определённые в роутере обработчики
    диспетчером.
    """
    dp.callback_query.register(
        handle_webinar_records, lambda call: call.data == "webinar_records"
    )
