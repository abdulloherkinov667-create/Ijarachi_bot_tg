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


def soni_kv(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n.gettext

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('1_')),
                KeyboardButton(text=_('2_')),
                KeyboardButton(text=_('3_')),
                KeyboardButton(text=_('4_')),
                KeyboardButton(text=_('5_'))
            ],
            [
                KeyboardButton(text=_('6_')),
                KeyboardButton(text=_('7_')),
                KeyboardButton(text=_('8_')),
                KeyboardButton(text=_('9_')),
                KeyboardButton(text=_('10_'))
            ],
        ],
        resize_keyboard=True
    )

    
    
    
def maydon_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n.gettext

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('m2_20')),
                KeyboardButton(text=_('m2_25')),
                KeyboardButton(text=_('m2_30')),
                KeyboardButton(text=_('m2_35')),
                KeyboardButton(text=_('m2_40'))
            ],
            [
                KeyboardButton(text=_('m2_45')),
                KeyboardButton(text=_('m2_50')),
                KeyboardButton(text=_('m2_55')),
                KeyboardButton(text=_('m2_60')),
                KeyboardButton(text=_('m2_65'))
            ],
            [
                KeyboardButton(text=_('m2_70')),
                KeyboardButton(text=_('m2_75')),
                KeyboardButton(text=_('m2_80')),
                KeyboardButton(text=_('m2_85')),
                KeyboardButton(text=_('m2_90'))
            ],
            [
                KeyboardButton(text=_('m2_95')),
                KeyboardButton(text=_('m2_100')),
                KeyboardButton(text=_('m2_200')),
                KeyboardButton(text=_('m2_300')),
                KeyboardButton(text=_('m2_400'))
            ],
            [
                KeyboardButton(text=_('m2_500')),
                KeyboardButton(text=_('m2_600')),
                KeyboardButton(text=_('m2_700')),
                KeyboardButton(text=_('m2_800')),
                KeyboardButton(text=_('m2_900'))
            ],
            [
                KeyboardButton(text=_('m2_1000')),
                KeyboardButton(text=_('m2_2000')),
                KeyboardButton(text=_('m2_3000')),
                KeyboardButton(text=_('m2_4000')),
                KeyboardButton(text=_('m2_5000'))
            ],
            [
                KeyboardButton(text=_('m2_6000')),
                KeyboardButton(text=_('m2_6500'))
            ],
            [
                KeyboardButton(text=_('ortaga_text')),
                KeyboardButton(text=_('bosh_sahifa_text'))
            ],
        ],
        resize_keyboard=True
    )
    
    
def ijarachilar_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n.gettext

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('talabalarga_text')),
                KeyboardButton(text=_('ishchilarga_text'))
            ],
            [
                KeyboardButton(text=_('sayyohlarga_text')),
                KeyboardButton(text=_('oilaga_text'))
            ],
            [
                KeyboardButton(text=_('sheriklikka_text')),
                KeyboardButton(text=_('barchaga_text'))
            ],
            [
                KeyboardButton(text=_('bosh_saxifa_text')),
                KeyboardButton(text=_('ortaga_text'))
            ],
        ],
        resize_keyboard=True
    )    