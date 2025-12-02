from aiogram import types, Router, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram_i18n.context import I18nContext
from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from models.users import User
from database import SessionLocal
from keyboard.defoul import (
    uylar_tur, tuman, maydon_menu, soni_kv,
    ijara_muddati, ijarachilar_menu, tamir_turi, texnika_buttons,
    dollar_buttons, foiz_button, tel_button, izoh, bosh_saxifa
)
from states import KvartiraBosh
from keyboard.inlayn import inline

dp = Router()




@dp.message(lambda message, i18n: message.text == i18n("ijaraga_beraman"))
async def kv_start(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(bino_ta=msg.text)
    await msg.answer(i18n("bino_s"), reply_markup=uylar_tur(i18n))
    await state.set_state(KvartiraBosh.kvartira_tan)
        
@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def ot(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))        
        
        
        
        
        
@dp.message(KvartiraBosh.kvartira_tan)
async def muddat_time(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(muddat_tan=msg.text)
    await msg.answer(i18n("muddat_text"), reply_markup=ijara_muddati(i18n))
    await state.set_state(KvartiraBosh.muddat_ijara)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def oat(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=uylar_tur(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def oqtdsd(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))       





@dp.message(KvartiraBosh.muddat_ijara)
async def manzil_kv(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(manzil_kv_tan=msg.text)
    await msg.answer(i18n("qaysi_tuman"), reply_markup=tuman(i18n))
    await state.set_state(KvartiraBosh.manzil)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def oaaat(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=ijara_muddati(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def obqaewft(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))     




@dp.message(KvartiraBosh.manzil)
async def kimlarga_tt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(kimlar_kv_tan=msg.text)
    await msg.answer(i18n("kimlarga_ber_text_kv_uz"), reply_markup=ijarachilar_menu(i18n))
    await state.set_state(KvartiraBosh.kimlarga_k)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def blat(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=tuman(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def obqdwefweft(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
    
        


@dp.message(KvartiraBosh.kimlarga_k)
async def xo_soni(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(son_tean_kv=msg.text)
    await msg.answer(i18n("kv_soni_text"), reply_markup=soni_kv(i18n))
    await state.set_state(KvartiraBosh.xona_soni)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def at(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=ijarachilar_menu(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def obqfwefwqqt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
    
    
        


@dp.message(KvartiraBosh.xona_soni)
async def kv_maydon(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(xona_maydon_kv=msg.text)
    await msg.answer(i18n("Kv_maydon_text"), reply_markup=maydon_menu(i18n))
    await state.set_state(KvartiraBosh.maydoni)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def bq__liat(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=soni_kv(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def olasdk_abqt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
        


@dp.message(KvartiraBosh.maydoni)
async def kvartira_ma(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(rasm_kv=msg.text)
    await msg.answer(i18n("rasm_sor"), reply_markup=izoh(i18n))
    await state.set_state(KvartiraBosh.rasm)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def bqatsan(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=maydon_menu(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def obqxasdask_at(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
    
        


@dp.message(KvartiraBosh.rasm, F.photo)
async def book_rasm(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(rasm_tashla_tex=msg.photo[-1].file_id)
    await msg.answer(i18n("tamir_sor_text"), reply_markup=tamir_turi(i18n))
    await state.set_state(KvartiraBosh.tamir)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def atsan(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=izoh(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def obqalalt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
    
        


@dp.message(KvartiraBosh.tamir)
async def jihoz_sor(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(tamir_text=msg.text)
    await msg.answer(i18n("jihoz_sor_text"), reply_markup=texnika_buttons(i18n))
    await state.set_state(KvartiraBosh.jihoz_uyda)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def atsakere(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=tamir_turi(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def oalqabqt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
    


@dp.message(KvartiraBosh.jihoz_uyda)
async def kv_narz(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(jihozlar=msg.text)
    await msg.answer(i18n("narx_sor_tex"), reply_markup=dollar_buttons(i18n))
    await state.set_state(KvartiraBosh.kvar_narx)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def kerak(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=texnika_buttons(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def oqoaxbqt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
    
        


@dp.message(KvartiraBosh.kvar_narx)
async def kv_haq(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(narx_rasm=msg.text)
    await msg.answer(i18n("vosita_haq_text"), reply_markup=foiz_button(i18n))
    await state.set_state(KvartiraBosh.kvar_vosita)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def kerakedi(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=dollar_buttons(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def pldcobqt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
        


@dp.message(KvartiraBosh.kvar_vosita)
async def kv_haq_tel(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(qaqqihaqi=msg.text)
    await msg.answer(i18n("tel_sor_text"), reply_markup=tel_button(i18n))
    await state.set_state(KvartiraBosh.user_tel)
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def kerakedichun(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=foiz_button(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def oapqsbqt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
    
    


@dp.message(KvartiraBosh.user_tel)
async def kv_izo(msg: types.Message, i18n: I18nContext, state: FSMContext):
    if msg.contact:
        await state.update_data(kv_tel=msg.contact.phone_number)
    else:
        await state.update_data(kv_tel=msg.text)

    data = await state.get_data()
    rasm_id = data.get("rasm_tashla_tex")
    kv_tel = data.get("kv_tel")

    if rasm_id:
        await msg.answer_photo(
            photo=rasm_id,
            caption=f"""
🌟 {i18n('ijara_chi_ber')} | {data.get('muddat_tan')}

📍 {i18n('manz_il')} : {i18n('tosh_ken')}, {data.get('kimlar_kv_tan')}
🛠️ {i18n('tam_ir')} : {data.get('tamir_text')}
📐 {i18n('maydo_ni')} : {data.get('rasm_kv')}
💵 {i18n('na_rx')} {i18n('narx_1_oy')} : {data.get('narx_rasm')}
🤝 {i18n('vosita_chilik')} : {data.get('qaqqihaqi')}
🔌 {i18n('jiho_zlar')} : {data.get('jihozlar')}


📱 {i18n('telefo_n')} : +{kv_tel}
{i18n('himcha_uz')} :@{msg.from_user.username}



📣 #{i18n('kana_l')}   📝 #{i18n('ol_x')}
👥 #{i18n('gur_uh')}   📷 #{i18n('instagra_m')}
""",
            reply_markup=ReplyKeyboardRemove()
        )

    await msg.answer(i18n("elon_tayyor_text"),reply_markup=inline(i18n))
    
# @dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
# async def ichun(msg: types.Message, i18n: I18nContext, state: FSMContext):
#     await msg.answer(i18n("qaytildi_text"), reply_markup=tel_button(i18n)) 

@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def ospzbqt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))    

        
@dp.message(lambda message, i18n: message.text == i18n("ortaga_text"))
async def ortga_qayt(msg: types.Message, i18n: I18nContext, state: FSMContext):
    current_state = await state.get_state()
    
    # if current_state == KvartiraBosh.kvartira_tan.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=uylar_tur(i18n))
    # elif current_state == KvartiraBosh.muddat_ijara.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=ijara_muddati(i18n))
    # elif current_state == KvartiraBosh.manzil.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=tuman(i18n))
    # elif current_state == KvartiraBosh.kimlarga_k.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=ijarachilar_menu(i18n))
    # elif current_state == KvartiraBosh.xona_soni.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=soni_kv(i18n))
    # elif current_state == KvartiraBosh.maydoni.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=maydon_menu(i18n))
    # elif current_state == KvartiraBosh.rasm.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=izoh(i18n))
    # elif current_state == KvartiraBosh.tamir.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=tamir_turi(i18n))
    # elif current_state == KvartiraBosh.jihoz_uyda.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=texnika_buttons(i18n))
    # elif current_state == KvartiraBosh.kvar_narx.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=dollar_buttons(i18n))
    # elif current_state == KvartiraBosh.kvar_vosita.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=foiz_button(i18n))
    # elif current_state == KvartiraBosh.user_tel.state:
    #     await msg.answer(i18n("qaytildi_text"), reply_markup=tel_button(i18n))

