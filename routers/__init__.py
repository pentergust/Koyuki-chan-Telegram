"""Список всех обработчиков бота.

Вы можете использовать данный файл для более детальной настройки функционала
обработчиков бота.
"""

from routers import (  # noqa: F401
    bot_help,
    bot_info,
    homework_help,
    homework_list,
    logging,
    main_menu,
    navigation,
    webinar_records,
)

# Список всех доступных обработчиков
ROUTERS = (
    bot_help,
    bot_info,
    homework_help,
    homework_list,
    # logging,
    main_menu,
    navigation,
    webinar_records,
)

# Из этого файла нам нужен лишь список обарботчиков
__all__ = ["ROUTERS"]
