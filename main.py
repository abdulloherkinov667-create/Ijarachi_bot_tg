import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, command
from pathlib import Path
from aiogram import types
from keyboard.defoul import till_button, bosh_menu, bosh_saxifa, uylar_tur
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv
from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from models.users import User
from database import SessionLocal
from handlers.kvartira import dp as kvartira_dp

 


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

dp = Dispatcher()
dp.update.middleware(i18n_middleware) 

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "uz")
SUPPORTED_LANGUAGES = ["uz", "ru", "en"]





@dp.message(CommandStart())
async def start(message: types.Message, i18n: I18nContext):
    await i18n.set_locale(message.from_user.language_code)
    try:
        db = SessionLocal()
        db_user = User(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        language_code=message.from_user.language_code,
        is_active=True
    )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        pass
    await message.answer(i18n("kop_till_text"), reply_markup=till_button(i18n))






# til uz
@dp.message(lambda message, i18n: message.text == i18n("uz"))
async def til_uz(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('uz')
    await msg.answer(i18n("xush_keldi_text"), reply_markup=bosh_saxifa(i18n))


#qanday ishlaydi uz
@dp.message(lambda message, i18n: message.text == i18n("qanday_ishlaydi"))
async def about(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('uz')
    await msg.answer(i18n("biz_xaqimizda"), reply_markup=bosh_menu(i18n))
    url = 'https://avatars.mds.yandex.net/i?id=b7937c3d1ffc42560b0662437c5359b8_sr-12994680-images-thumbs&n=13'
    text = """
IJARA-CHI loyihasi ishlash tartibi

1) Ijaraga bermoqchi bo‘lsangiz Ijaraga beraman tugmasini bosing, kerakli bo‘limlar bo‘yicha ma’lumotlarni kiriting va mijozlar qo‘ng‘iroqlarini kuting!

2) IJARA-CHI O‘zbek, Rus va Ingliz tillarida faoliyat yuritadi.

✏️ TAKLIFLARNI BIZGA YOZING (https://t.me/IJARA_CHI_ADMIN)

Discovery Consult MCHJ xizmat ko‘rsatadi.
"""
    await msg.answer_photo(url, caption=text)
    
   
@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def change_uz(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('uz')
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))  
    
   
    
    
    
    
    
      











# til ru
@dp.message(lambda message, i18n: message.text == i18n("ru"))
async def til_ru(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('ru')
    await msg.answer(i18n("xush_keldi_text"), reply_markup=bosh_saxifa(i18n))


# qanday ishlaydi ru
@dp.message(lambda message, i18n: message.text == i18n("qanday_ishlaydi"))
async def about_ru(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('ru')
    await msg.answer(i18n("biz_xaqimizda"), reply_markup=bosh_menu(i18n))
    
    url = 'https://avatars.mds.yandex.net/i?id=b7937c3d1ffc42560b0662437c5359b8_sr-12994680-images-thumbs&n=13'
    text = """
Как работает проект IJARA-CHI

1) Если вы хотите сдать в аренду, нажмите кнопку «Сдать в аренду», заполните информацию по нужным категориям и ждите звонков от клиентов!

2) IJARA-CHI работает на узбекском, русском и английском языках.

✏️ ПИШИТЕ НАМ СВОИ ПРЕДЛОЖЕНИЯ (https://t.me/IJARA_CHI_ADMIN)

Услугу предоставляет Discovery Consult ООО.
"""
    await msg.answer_photo(url, caption=text)


@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def change_ru(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('ru')
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))
        
    
    
    
    












# language en
@dp.message(lambda message, i18n: message.text == i18n("en"))
async def lang_en_start(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('en')
    await msg.answer(i18n("xush_keldi_text"), reply_markup=bosh_saxifa(i18n))


# how it works (EN)
@dp.message(lambda message, i18n: message.text == i18n("qanday_ishlaydi"))
async def lang_en_about(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('en')
    await msg.answer(i18n("biz_xaqimizda"), reply_markup=bosh_menu(i18n))

    url = 'https://avatars.mds.yandex.net/i?id=b7937c3d1ffc42560b0662437c5359b8_sr-12994680-images-thumbs&n=13'
    text = """
How IJARA-CHI works

1) If you want to rent out your property, press the "Rent out" button, fill in the required information, and wait for client calls!

2) IJARA-CHI operates in Uzbek, Russian, and English languages.

✏️ SEND US YOUR SUGGESTIONS (https://t.me/IJARA_CHI_ADMIN)

Service provided by Discovery Consult LLC.
"""
    await msg.answer_photo(url, caption=text)


@dp.message(lambda message, i18n: message.text == i18n("bosh_saxifa_text"))
async def lang_en_home(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('en')
    await msg.answer(i18n("qaytildi_text"), reply_markup=bosh_saxifa(i18n))


    
    
    
    
    
      
    
     











async def main():
    bot = Bot(token=BOT_TOKEN)
    i18n_middleware.setup(dispatcher=dp)
    await dp.start_polling(bot)
    dp.include_router(kvartira_dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())