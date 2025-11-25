from aiogram import types, Router, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext
from keyboard.defoul import uylar_tur, bosh_saxifa, tuman, ijara_muddati, ijarachilar_menu
from states import KvartiraBosh



dp = Router()

@dp.message(lambda message, i18n: message.text == i18n("ijaraga_beraman"))
async def kv_start(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.set_state(KvartiraBosh.kvartira_tan)
    await msg.answer(i18n("bino_s"), reply_markup=uylar_tur(i18n))
    
    
@dp.message(KvartiraBosh.kvartira_tan)
async def muddat_time(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(kvartira_tan = msg.text)
    await state.set_state(KvartiraBosh.muddat_ijara)
    await msg.answer(i18n("muddat_text"), reply_markup=ijara_muddati(i18n))    
    
    
@dp.message(KvartiraBosh.muddat_ijara)
async def manzil_kv(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(manzil_kv_tan = msg.text)
    await state.set_state(KvartiraBosh.manzil)
    await msg.answer(i18n("qaysi_tuman"), reply_markup=tuman(i18n))   
    
    
@dp.message(KvartiraBosh.manzil)
async def kimlarga_tt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(manzil_kv_tan = msg.text)
    await state.set_state(KvartiraBosh.kimlarga_k)
    await msg.answer(i18n("kv_kimlarga"), reply_markup=ijarachilar_menu(i18n))  
    
    
@dp.message(KvartiraBosh.kimlarga_k)
async def xo_soni(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(manzil_kv_tan = msg.text)
    await state.set_state(KvartiraBosh.xona_soni)
    await msg.answer(i18n("kv_kimlarga"), reply_markup=ijarachilar_menu(i18n))                                           
    
    
    
    
    
 # @dp.message(F.text == "Kivartira")
# async def k(message: types.Message, state: FSMContext):
#     await message.answer("Qancha muddatga ijaraga berasiz?")
#     await state.set_state(Register.holati)   
    
    
@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def change_til_uz(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('uz')
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    