from aiogram_i18n import I18nContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def till_button(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('ru')),
                KeyboardButton(text=_('en')),
                KeyboardButton(text=_('uzbe'))
            ]
        ],
        resize_keyboard=True
    )    