from aiogram import types, Router, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext
from keyboard.defoul import uylar_tur, bosh_saxifa, tuman, ijara_muddati, ijarachilar_menu, maydon_menu, soni_kv
from states import KvartiraBosh
from aiogram.filters import CommandStart, command




dp = Router()


@dp.message(lambda message, i18n: message.text == i18n("ijaraga_beraman"))
async def kv_start(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await msg.answer(i18n("bino_s"), reply_markup=uylar_tur(i18n))
    await state.set_state(KvartiraBosh.kvartira_tan)    
    
    
@dp.message(KvartiraBosh.kvartira_tan)
async def muddat_time(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(muddat_tan = msg.text)
    await msg.answer(i18n("muddat_text"), reply_markup=ijara_muddati(i18n))    
    await state.set_state(KvartiraBosh.muddat_ijara)
    
    
@dp.message(KvartiraBosh.muddat_ijara)
async def manzil_kv(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(manzil_kv_tan = msg.text)
    await msg.answer(i18n("qaysi_tuman"), reply_markup=tuman(i18n))   
    await state.set_state(KvartiraBosh.manzil)
    
    
@dp.message(KvartiraBosh.manzil)
async def kimlarga_tt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(kimlar_kv_tan = msg.text)
    await msg.answer(i18n("qaysi_tuman"), reply_markup=tuman(i18n))  
    await state.set_state(KvartiraBosh.kimlarga_k)
    
    
@dp.message(KvartiraBosh.kimlarga_k)
async def xo_soni(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(xona_kv_tan = msg.text)
    await msg.answer(i18n("kv_kimlarga"), reply_markup=ijarachilar_menu(i18n))                                           
    await state.set_state(KvartiraBosh.xona_soni)
    

@dp.message(KvartiraBosh.xona_soni)
async def kv_maydon(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(xona_kv_son = msg.text)
    await msg.answer(i18n("kv_soni_text"), reply_markup=soni_kv(i18n)) 
    await state.set_state(KvartiraBosh.maydoni)
    
    
@dp.message(KvartiraBosh.maydoni)
async def book_rasm(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(maydon_kv_user = msg.text)
    await msg.answer(i18n("Kv_maydon_text", reply_markup =maydon_menu(i18n)))
    await state.set_state(KvartiraBosh.rasm)  
    
    
# @dp.message(KvartiraBosh.rasm, F.photo)
# async def book_rasm(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await i18n.set_locale('uz')
#     await state.update_data(kv_rasm = msg.photo[-1])
#     await msg.answer(i18n("rasm_sor_text", reply_markup =maydon_menu(i18n)))
#     await state.set_state(KvartiraBosh.rasm)       