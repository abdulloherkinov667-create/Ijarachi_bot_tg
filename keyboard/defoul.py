from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 
from aiogram_i18n import I18nContext
import sqlite3
from aiogram_i18n.context import I18nContext

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