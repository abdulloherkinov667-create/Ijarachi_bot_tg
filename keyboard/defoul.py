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
    _ = i18n

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
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=("1_")),
                KeyboardButton(text=("2_")),
                KeyboardButton(text=("3_")),
                KeyboardButton(text=("4_")),
                KeyboardButton(text=("5_"))
            ],
            [
                KeyboardButton(text=("6_")),
                KeyboardButton(text=("7_")),
                KeyboardButton(text=("8_")),
                KeyboardButton(text=("9_")),
                KeyboardButton(text=("10_"))
            ],
        ],
        resize_keyboard=True
    )


def maydon_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

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
                KeyboardButton(text=_('bosh_saxifa_text'))
            ],
        ],
        resize_keyboard=True
    )
    
    
def ijarachilar_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

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
    
    
def tamir_turi(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('yevro_tamir')),
                KeyboardButton(text=_('ta_misz'))
            ],
            [
                KeyboardButton(text=_('karop_ka')),
                KeyboardButton(text=_('orta_tamir'))
            ],
            [
                KeyboardButton(text=_('ortaga_text')),
                KeyboardButton(text=_('bosh_saxifa_text'))
            ],
        ],
        resize_keyboard=True
    )     
    
    
def texnika_buttons(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("tv")),
                KeyboardButton(text=_("muzlatgich")),
                KeyboardButton(text=_("konditsioner"))
            ],
            [
                KeyboardButton(text=_("changyutgich")),
                KeyboardButton(text=_("mikroto_lqin")),
                KeyboardButton(text=_("ventilyator")),
            ],
            [
                KeyboardButton(text=_("choynak")),
                KeyboardButton(text=_("wifi")),
                KeyboardButton(text=_("isitgich"))
            ],
            [
                
                KeyboardButton(text=_("bosh_saxifa_text")),
                KeyboardButton(text=_("ortaga_text"))
            ]
        ],
        resize_keyboard=True
    )
    

def dollar_buttons(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("100")),
                KeyboardButton(text=_("200")),
                KeyboardButton(text=_("300")),
                KeyboardButton(text=_("400")),
                KeyboardButton(text=_("500"))
            ],
            [
                KeyboardButton(text=_("600")),
                KeyboardButton(text=_("700")),
                KeyboardButton(text=_("800")),
                KeyboardButton(text=_("900")),
                KeyboardButton(text=_("1000"))
            ],
            [
                KeyboardButton(text=_("1500")),
                KeyboardButton(text=_("2000")),
                KeyboardButton(text=_("2500")),
                KeyboardButton(text=_("3000")),
                KeyboardButton(text=_("3500"))
            ],
            [
                KeyboardButton(text=_("4000$")),
                KeyboardButton(text=_("4500$")),
                KeyboardButton(text=_("5000$")),
                KeyboardButton(text=_("bosh_saxifa_text")),
                KeyboardButton(text=_("ortaga_text"))
            ]
        ],
        resize_keyboard=True
    )
    
    
def foiz_button(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("yo"))
            ],
            [
                KeyboardButton(text=_("5%")),
                KeyboardButton(text=_("10%")),
                KeyboardButton(text=_("15%")),
                KeyboardButton(text=_("20%")),
                KeyboardButton(text=_("25%"))
            ],
            [
                KeyboardButton(text=_("30%")),
                KeyboardButton(text=_("35%")),
                KeyboardButton(text=_("40%")),
                KeyboardButton(text=_("45%")),
                KeyboardButton(text=_("50%"))
            ],
            [
                KeyboardButton(text=_("bosh_saxifa_text")),
                KeyboardButton(text=_("ortaga_text"))
            ]
        ],
        resize_keyboard=True
    )  
    
    
def tel_button(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("tel_button_text"), request_contact=True)
            ]
        ],
        resize_keyboard=True
        )  
    
    
def izoh(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("tel_button_text"), request_contact=True)
            ], 
            [
                KeyboardButton(text=_("bosh_saxifa_text")),
                KeyboardButton(text=_("ortaga_text"))
            ]
        ],
        resize_keyboard=True
        )        