from aiogram import Dispatcher, types


async def handle_help(call: types.CallbackQuery):
    text = """
    **ПОМОЩЬ**

    Добро пожаловать в раздел помощи Koyuki-chan! Выберите один из разделов ниже:
    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📝 Помощь с ДЗ", callback_data="homework_help")],
        [types.InlineKeyboardButton(text="❓ Частые вопросы", callback_data="faq")],
        [types.InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

async def handle_faq(call: types.CallbackQuery):
    text = """
    **ЧАСТЫЕ ВОПРОСЫ (FAQ)**

    Выберите один из разделов ниже:
    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📖 Ликбез", callback_data="basics")],
        [types.InlineKeyboardButton(text="📚 Инструкция по LMS", callback_data="lms_guide")],
        [types.InlineKeyboardButton(text="✉️ Написать куратору", callback_data="contact_curator")],
        [types.InlineKeyboardButton(text="⬅️ Назад в помощь", callback_data="help")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

async def handle_basics(call: types.CallbackQuery):
    text = """
    **ЛИКБЕЗ**

    👩‍🏫 **Преподаватель/Лектор** - к ним можно обращаться, если возникают вопросы о материале, пройденном на вебинаре.

    👨‍💻 **Тьюторы** - опытные программисты, которые помогут с освоением учебного материала. Они проверят домашние работы и подскажут, если возникнут сложности с заданиями.

    🛟 **Кураторы** (Анастасия @plastasya и Яна @qtwec) - спасательный круг, справочный центр, ваша фея-крестная с тапочкой вместо волшебной палочки (тапочка ускоряет сдачу ДЗ вне зависимости от обстоятельств). 
    Ей можно задать любой вопрос, ответ на который не найден в канале. Она поможет всем и всегда, особенно если написать заранее. 
    Единственный минус - куратор не программист, так что если вопрос о способе выполнения домашней работы - вас отправят к тьютору. Если тьютор долго не отвечает - пишем об этом куратору.

    📚 **ЛМС** - система, в которой вы будете выполнять домашние задания.

    💻 **МТС Линк** - платформа для просмотра вебинаров.
    Кто будет смотреть вебинар с ПК, ноутбука - просто открывайте ссылку на вебинар.
    Если вы смотрите вебинар с телефона - качайте приложение. 
    Пожалуйста, не перепутайте!

    📅 **Срок сдачи ДЗ** - даты, к которым нужно выполнить домашние задания и тест, если не хотите получать миллион звонков от других кураторов/менеджеров (родителям тоже будем звонить, да).
    Если у вас есть какие-то трудности с домашними заданиями, не хватает времени, нет желания вообще, то скажите своему куратору об этом сразу, а не игнорируйте.
    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⬅️ Назад в частые вопросы", callback_data="faq")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

async def handle_lms_guide(call: types.CallbackQuery):
    text = """
    **ИНСТРУКЦИЯ ПО LMS**

    В этом разделе вы найдете руководство по использованию LMS.

    Полная инструкция доступна по ссылке: [ссылка](https://telegra.ph/INSTRUKCIYA-PO-POLZOVANIYU-LMS-07-24)
    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⬅️ Назад в частые вопросы", callback_data="faq")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

async def handle_contact_curator(call: types.CallbackQuery):
    text = """
    **НАПИСАТЬ КУРАТОРУ**

    Если у вас есть вопросы или предложения, свяжитесь с одним из наших кураторов:

    👩‍🏫 **Преподаватель:** Игорь Мишин [@Imishinigor](https://t.me/Imishinigor)
    👨‍💻 **Тьютор:** Александр Головачев [@YourBuduschee2](https://t.me/YourBuduschee2)
    🛟 **Кураторы:** Анастасия [@plastasya](https://t.me/plastasya) и Яна [@qtwec](https://t.me/qtwec)
    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⬅️ Назад в частые вопросы", callback_data="faq")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(handle_help, lambda call: call.data == "help")
    dp.callback_query.register(handle_faq, lambda call: call.data == "faq")
    dp.callback_query.register(handle_basics, lambda call: call.data == "basics")
    dp.callback_query.register(handle_lms_guide, lambda call: call.data == "lms_guide")
    dp.callback_query.register(handle_contact_curator, lambda call: call.data == "contact_curator")
