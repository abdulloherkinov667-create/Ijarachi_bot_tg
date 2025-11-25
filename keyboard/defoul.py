from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import I18nContext


def till_button(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('ru')),
                KeyboardButton(text=_('en')),
                KeyboardButton(text=_('uz'))
            ]
        ],
        resize_keyboard=True
    )    
    
    
    
    
def bosh_saxifa(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('ijara_text')),
                KeyboardButton(text=_('ijaraga_beraman'))
            ],

            [
                KeyboardButton(text=_('tilni_tanlash_text')),
                KeyboardButton(text=_('qanday_ishlaydi'))
            ],
        ],
        resize_keyboard=True
    )   
    
    
    
    
def bosh_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('bosh_saxifa_text'))
            ]
        ],
        resize_keyboard=True
    )    
    
    
    
def uylar_tur(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            
        ],
        resize_keyboard=True
    ) 
    
    
def uylar_tur(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('kv_artira')),
                KeyboardButton(text=_('Uy_hovli'))
            ],

            [
                KeyboardButton(text=_('D_acha')),
                KeyboardButton(text=_('o_fis'))
            ],
            [
                KeyboardButton(text=_('bosh_saxifa_text'))
            ]
        ],
        resize_keyboard=True
    )    
    
    
    
def ijara_muddati(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('uzoq_text')),
                KeyboardButton(text=_('kunlik_text'))
            ],

            [
                KeyboardButton(text=_('ortaga_text')),
                KeyboardButton(text=_('bosh_saxifa_text'))
            ],
        ],
        resize_keyboard=True
    ) 
    
    
    
def tuman(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n.gettext

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('tanlash_shaxar'))
            ],
            [
                KeyboardButton(text=_('olmazor_text')),
                KeyboardButton(text=_('bektemir_text')),
                KeyboardButton(text=_('mirobod_text'))
            ],
            [
                KeyboardButton(text=_('yunusobod_text')),
                KeyboardButton(text=_('chilonzor_text')),
                KeyboardButton(text=_('sergeli_text'))
            ],
            [
                KeyboardButton(text=_('shayxontohur_text')),
                KeyboardButton(text=_('uchtepa_text')),
                KeyboardButton(text=_('yashnobod_text'))
            ],
        ],
        resize_keyboard=True
    )     
    
    


def ijarachilar_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n.gettext

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('talabalar_text')),
                KeyboardButton(text=_('ishchilar_text'))
            ],
            [
                KeyboardButton(text=_('sayyohlar_text')),
                KeyboardButton(text=_('oilaga_text'))
            ],
            [
                KeyboardButton(text=_('sheriklik_text')),
                KeyboardButton(text=_('barchaga_text'))
            ],
            [
                KeyboardButton(text=_('ortaga_text')),
                KeyboardButton(text=_('bosh_sahifa_text'))
            ],
        ],
        resize_keyboard=True
    )
    
    