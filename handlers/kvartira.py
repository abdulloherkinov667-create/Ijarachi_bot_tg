from aiogram import types, Router, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext
from aiogram.filters import CommandStart, command
from keyboard.defoul import uylar_tur, bosh_saxifa, tuman, maydon_menu, soni_kv, ijara_muddati, ijarachilar_menu, tamir_turi, texnika_buttons, dollar_buttons, foiz_button, tel_button, izoh
from states import KvartiraBosh





dp = Router()


@dp.message(lambda message, i18n: message.text == i18n("ijaraga_beraman"))
async def kv_start(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(bino_ta = msg.text)
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
    await msg.answer(i18n("kimlarga_ber_text_kv_uz"), reply_markup=ijarachilar_menu(i18n))  
    await state.set_state(KvartiraBosh.kimlarga_k)
    
    
@dp.message(KvartiraBosh.kimlarga_k)
async def xo_soni(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(son_tean_kv = msg.text)
    await msg.answer(i18n("kv_soni_text"), reply_markup=soni_kv(i18n))                                           
    await state.set_state(KvartiraBosh.xona_soni)
    

@dp.message(KvartiraBosh.xona_soni)
async def kv_maydon(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(xona_maydon_kv = msg.text)
    await msg.answer(i18n("Kv_maydon_text"), reply_markup=maydon_menu(i18n)) 
    await state.set_state(KvartiraBosh.maydoni)
    
    
@dp.message(KvartiraBosh.maydoni)
async def kvartira_ma(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(rasm_kv = msg.text)
    await i18n.set_locale('uz')
    await msg.answer(i18n("rasm_sor"), reply_markup=ReplyKeyboardRemove())
    await state.set_state(KvartiraBosh.rasm)


@dp.message(KvartiraBosh.rasm, F.photo)
async def book_rasm(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(rasm_tashla_tex = msg.photo[-1])
    await msg.answer(i18n("tamir_sor_text"), reply_markup=tamir_turi(i18n))
    await state.set_state(KvartiraBosh.tamir)
    
    
@dp.message(KvartiraBosh.tamir)
async def jihoz_sor(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(jihoz_user = msg.text)
    await msg.answer(i18n("jihoz_sor_text"), reply_markup =texnika_buttons(i18n))
    await state.set_state(KvartiraBosh.jihoz_uyda) 
    
    
@dp.message(KvartiraBosh.jihoz_uyda)
async def kv_narz(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(kvnarx_rasm = msg.text)
    await msg.answer(i18n("narx_sor_tex"), reply_markup =dollar_buttons(i18n))
    await state.set_state(KvartiraBosh.kvar_vosita)
    
    
@dp.message(KvartiraBosh.kvar_vosita)
async def kv_haq(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(kv_haqi = msg.text)
    await msg.answer(i18n("vosita_haq_text"), reply_markup =foiz_button(i18n))
    await state.set_state(KvartiraBosh.kvar_vosita)    
    
    
@dp.message(KvartiraBosh.kvar_vosita)
async def kv_haq_tel(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(kv_tel = msg.text)
    await msg.answer(i18n("tel_sor_text"), reply_markup =tel_button(i18n))
    await state.set_state(KvartiraBosh.izoh_user)    
    
    
@dp.message(KvartiraBosh.izoh_user)
async def kv_izo(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await i18n.set_locale('uz')
    await state.update_data(izoh = msg.text)
    await state.update_data(izoh = msg.text)
    data = await state.get_data()
    
    data2 = f"""
    {data.get('rasm_tashla_tex')}
    
    🌟IJARA-CHI | {data.get('bino_ta')}
    
    
    📍 Manzil: Toshkent, {data.get('manzil_kv_tan')}
    🛠️ Ta'mir: {data.get('tamir_text')}
    📐 Maydoni: {data.get('xona_maydon_kv')}
    💵 Narxi: {data.get('kvnarx_rasm')}
    🤝 Vositachilik haqi: {data.get('kv_haqi')}
    🔌 Jihozlar:  {data.get('jihoz_user')}
    
    
    📱 <-- {data.get('tel_sor_text')}
    
    
    
    📣 KANAL  📝 OLX
    👥 GURUH  📷 INSTAGRAM 

    """  
    await msg.answer(data2)