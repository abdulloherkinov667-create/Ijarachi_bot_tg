import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from pathlib import Path
from aiogram import types

from dotenv import load_dotenv
# from middlewares.i18n import i18n_middleware
# from aiogram_i18n.context import I18nContext

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")



dp = Dispatcher()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "uz")
SUPPORTED_LANGUAGES = ["uz", "ru", "en"]


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Salom")



async def main():
    bot = Bot(token=BOT_TOKEN)
    # i18n_middleware.setup(dispatcher=dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())