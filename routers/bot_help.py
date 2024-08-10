"""Раздел помощи.

Данный роутер предоставляет доступ к разделу помощи.
тут вы можете получить доступ к часто задаваемым вопросам,
обратиться за помощью в решении дз.

Предоставляет
-------------

- /help (help) - раздел помощи по боту.
- /faq (faq) - часто задаваемые вопросы
- basics - Всё что нужно знать для начала.
- lms_guide - Инструкция как можно пользоваться LSM.
- contact_curator - Как связаться с куратором.
"""

from aiogram import Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

# Глобальные переменные
# =====================

router = Router(name=__name__)


# Раздел помощи ----------------------------------------------------------------

HELP_MESSAGE = (
    "*Раздел помощи:*\n\n"
    "Если вы столкнулись с трудностями, я буду рада вам помочь чем смогу\n"
    "Выберите один из вариантов ниже:"
)

HELP_MARKUP = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="📝 Помощь с ДЗ", callback_data="homework_help"
    )],
    [InlineKeyboardButton(
        text="❓ Частые вопросы", callback_data="faq"
    )],
    [InlineKeyboardButton(
        text="⬅️ Назад в меню", callback_data="back_to_menu"
    )]
])

# Часто задаваемые вопросы -----------------------------------------------------

FAQ_MESSAGE = (
    "**Часто задаваемые вопросы (FAQ)**:\n\n"
    "У вас есть какие-то вопросы?\n"
    "Проверьте данный раздел, может на него уже есть ответ здесь\n"
    "Будем экономить выше время и время куратора\n\n"
    "Выберите один из разделов ниже:"
)

FAQ_MARKUP = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="📖 Ликбез", callback_data="basics"
    )],
    [InlineKeyboardButton(
        text="📚 Инструкция по LMS", callback_data="lms_guide"
    )],
    [InlineKeyboardButton(
        text="✉️ Написать куратору", callback_data="contact_curator"
    )],
    [InlineKeyboardButton(
        text="⬅️ Назад в помощь", callback_data="help"
    )]
])

TO_FAQ_MARKUP = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="⬅️ Назад в частые вопросы", callback_data="faq")
]])

# Немножко про базу ------------------------------------------------------------

BASICS_MESSAGE = (
    "*ЛИКБЕЗ*\n\n."
    "👩‍🏫 *Преподаватель/Лектор* - к ним можно обращаться, если возникают"
    "вопросы о материале, пройденном на вебинаре\n\n"
    "👨‍💻 *Тьюторы* - опытные программисты, которые помогут с освоением"
    "учебного материала Они проверят домашние работы и подскажут,"
    "если возникнут сложности с заданиями\n\n"
    "🛟 *Кураторы* (Анастасия @plastasya и Яна @qtwec) - спасательный круг,"
    "справочный центр, ваша фея-крестная с тапочкой вместо волшебной палочки"
    "(тапочка ускоряет сдачу ДЗ вне зависимости от обстоятельств)\n"
    "Ей можно задать любой вопрос, ответ на который не найден в канале"
    "Она поможет всем и всегда, особенно если написать заранее\n"
    "Единственный минус - куратор не программист, так что если вопрос о способе"
    "выполнения домашней работы - вас отправят к тьютору Если тьютор долго не"
    "отвечает - пишем об этом куратору\n\n"
    "📚 *ЛМС* - система, в которой вы будете выполнять домашки\n\n"
    "💻 *МТС Линк* - платформа для просмотра вебинаров\n"
    "Кто будет смотреть вебинар с ПК, ноутбука -"
    "просто открывайте ссылку на вебинар\n"
    "Если вы смотрите вебинар с телефона - качайте приложение\n"
    "Пожалуйста, не перепутайте!\n\n"
    "📅 *Срок сдачи ДЗ* - даты, к которым нужно выполнить домашние задания"
    "и тест, если не хотите получать миллион звонков от других"
    "кураторов/менеджеров (родителям тоже будем звонить, да)\n"
    "Если у вас есть какие-то трудности с домашними заданиями, не хватает"
    "времени, нет желания вообще, то скажите своему куратору об этом сразу,"
    "а не игнорируйте"
)

LMS_GUIDE_MESSAGE = (
    "*ИНСТРУКЦИЯ ПО LMS*\n\n"
    "В этом разделе вы найдете руководство по использованию LMS\n\n"
    "Полная инструкция доступна по ссылке:"
    " [ссылка](https://telegra.ph/INSTRUKCIYA-PO-POLZOVANIYU-LMS-07-24)"
)

CONTACT_CURATOR_MESSAGE = (
    "*НАПИСАТЬ КУРАТОРУ*\n\n"
    "Если у вас есть вопросы или предложения, свяжитесь с одним из"
    "наших кураторов:\n\n"
    "👩‍🏫 *Преподаватель:* Игорь Мишин"
    "[@Imishinigor](https://t.me/Imishinigor)\n"
    "👨‍💻 *Тьютор:* Александр Головачев"
    "[@YourBuduschee2](https://t.me/YourBuduschee2)\n"
    "🛟 *Кураторы:* Анастасия"
    "[@plastasya](https://t.me/plastasya) и Яна"
    "[@qtwec](https://t.me/qtwec)"
)


# Обработчики
# ===========

@router.message(Command("help"))
async def help_cmd(message: Message):
    """Отправялет нас в раздел получения поиощи.

    Тут пользователь сможет получить ответы на частые вопросы.
    Узнать к кому он может обратиться за помощью при решении проблем.
    А также получить решения для домашних заданий и теста.
    """
    await message.answer(
        text=HELP_MESSAGE, reply_markup=HELP_MARKUP
    )

@router.callback_query(F.data=="help")
async def help_call(query: CallbackQuery):
    """Отправялет нас в раздел получения поиощи.

    Тут пользователь сможет получить ответы на частые вопросы.
    Узнать к кому он может обратиться за помощью при решении проблем.
    А также получить решения для домашних заданий и теста.
    """
    await query.message.edit_text(
        text=HELP_MESSAGE, reply_markup=HELP_MARKUP
    )


@router.message(Command("faq"))
async def faq_cmd(message: Message):
    """Раздел часто задаваемых вопросов.

    Тут пользователь может получить заготовленный ответ, на самые часто
    задаемые вопросы во время обучения.
    """
    await message.answer(
        text=FAQ_MESSAGE, reply_markup=FAQ_MARKUP
    )

@router.callback_query(F.data=="faq")
async def faq_call(query: CallbackQuery):
    """Раздел часто задаваемых вопросов.

    Тут пользователь может получить заготовленный ответ, на самые часто
    задаемые вопросы во время обучения.
    """
    await query.message.edit_text(
        text=FAQ_MESSAGE, reply_markup=FAQ_MARKUP
    )


@router.callback_query(F.data=="basics")
async def basics_call(query: CallbackQuery):
    """Базовая информация.

    Тут пользователь сразу получает всю самую необходимую информацию.
    Кто такие кураторы, тьюторы, преподаватели, лмс и так далее.
    """
    await query.message.edit_text(
        text=BASICS_MESSAGE, reply_markup=TO_FAQ_MARKUP
    )

@router.callback_query(F.data=="lms_guide")
async def lms_call(query: CallbackQuery):
    """Как работать с ЛМС.

    В этом разделе находится материалы о том, как пользоватею начать
    пользовать ЛМС и что это вообще такое.
    """
    await query.message.edit_text(
        text=LMS_GUIDE_MESSAGE, reply_markup=TO_FAQ_MARKUP
    )

@router.callback_query(F.data=="contact_curator")
async def curator_call(query: CallbackQuery):
    """Связь с куратором.

    В этом разделе можно узнать, как пользователь может связаться
    с кураторами/тьюторами/преподавателями для получения помощи.
    """
    await query.message.edit_text(
        text=CONTACT_CURATOR_MESSAGE, reply_markup=TO_FAQ_MARKUP
    )


# Загрузчик роутера
# =================

def register_handlers(dp: Dispatcher) -> None:
    """Загрузчик обработчика.

    Данная функция вызывается при запуске бота.
    Она добавляет роутер к диспетчеру.
    Это позволяет использовать определённые в роутере обработчики
    диспетчером.
    """
    dp.include_router(router)
