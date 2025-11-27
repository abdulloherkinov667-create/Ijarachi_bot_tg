from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram_i18n import I18nContext

def inline(i18n) ->InlineKeyboardMarkup:
    _ = i18n

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("rh_au"), callback_data="rh"),
                InlineKeyboardButton(text=_("y_o"), callback_data="yo"),
            ],
            [
                InlineKeyboardButton(text=_("bosh_saxifa_text"), callback_data="boshsax"),
                InlineKeyboardButton(text=_("ortaga_text"), callback_data="ort"),
            ]
        ]
    )