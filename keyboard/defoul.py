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
                KeyboardButton(text=_('olmazor_text'))
            ],
            [
                KeyboardButton(text=_('bektemir_text'))
            ],
            [
                KeyboardButton(text=_('mirobod_text'))
            ],
            [
                KeyboardButton(text=_('yunusobod_text'))                
            ],
            [
                KeyboardButton(text=_('chilonzor_text'))                
            ],
            [
                KeyboardButton(text=_('sergeli_text'))
            ],
            [
                KeyboardButton(text=_('shayxontohur_text'))
            ],
            [
                KeyboardButton(text=_('uchtepa_text'))
            ],
            [
                KeyboardButton(text=_('yashnobod_text'))
            ],
            [
                KeyboardButton(text=_('ortaga_text')),
                KeyboardButton(text=_('bosh_saxifa_text'))
            ],
        ],
        resize_keyboard=True
    )        


def soni_kv(i18n: I18nContext) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=("1")),
                KeyboardButton(text=("2")),
                KeyboardButton(text=("3")),
                KeyboardButton(text=("4")),
                KeyboardButton(text=("5"))
            ],
            [
                KeyboardButton(text=("6")),
                KeyboardButton(text=("7")),
                KeyboardButton(text=("8")),
                KeyboardButton(text=("9")),
                KeyboardButton(text=("10"))
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
                KeyboardButton(text=_("muzlatgich"))
            ],
            [
                KeyboardButton(text=_("changyutgich")),
                KeyboardButton(text=_("mikroto_lqin")),
            ],
            [
                KeyboardButton(text=_("choynak")),                      
                KeyboardButton(text=_("ventilyator"))
            ],
            [
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
                KeyboardButton(text=_("y_text")),
                KeyboardButton(text=_("i_text")),
                KeyboardButton(text=_("u_text")),
                KeyboardButton(text=_("t_text")),
                KeyboardButton(text=_("b_text"))
            ],
            [
                KeyboardButton(text=_("o_text")),
                KeyboardButton(text=_("yo_text")),
                KeyboardButton(text=_("s_text")),
                KeyboardButton(text=_("t_text")),
                KeyboardButton(text=_("yu_text"))
            ],
            [
                KeyboardButton(text=_("iy_text")),
                KeyboardButton(text=_("im_text")),
                KeyboardButton(text=_("iy_text")),
                KeyboardButton(text=_("uyr_text")),
                KeyboardButton(text=_("uchra_text"))
            ],
            [
                KeyboardButton(text=_("tor_text")),
                KeyboardButton(text=_("text_tyar")),
                KeyboardButton(text=_("besh_text")),
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
                KeyboardButton(text=_("y_o"))
            ],
            [
                KeyboardButton(text=_("bes_h")),
                KeyboardButton(text=_("on_text")),
                KeyboardButton(text=_("onbes_h")),
                KeyboardButton(text=_("yigrm_a")),
                KeyboardButton(text=_("yigrmab_s"))
            ],
            [
                KeyboardButton(text=_("ots_t")),
                KeyboardButton(text=_("otiz_b")),
                KeyboardButton(text=_("qir_q")),
                KeyboardButton(text=_("qirs_sh")),
                KeyboardButton(text=_("eli_k"))
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
                KeyboardButton(text=_("bosh_saxifa_text")),
                KeyboardButton(text=_("ortaga_text"))
            ]
        ],
        resize_keyboard=True
        )        