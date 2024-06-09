from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_dialog import setup_dialogs

from config import BOT_TOKEN

from Routers.songs import song_router

from Menu.dialog import dialog
from Menu.dialogs.song_dialog.dialog import song_dialog
from Menu.dialogs.education_dialog.dialog import education_dialog
from Menu.dialogs.education_dialog.piggy_bank_dialog.dialog import (piggy_bank_dialog)

from Middleware.middleware import CheckUserRegistration, Mute

bot = Bot(token=BOT_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)

# TODO Требует реализации
# dp.message.outer_middleware(Mute())

dp.update.outer_middleware(CheckUserRegistration())

dp.include_router(song_router)

# Подключаем диалоги меню
dp.include_router(dialog)
dp.include_router(song_dialog)
dp.include_router(education_dialog)
dp.include_router(piggy_bank_dialog)

# Регистрируем диалоги
setup_dialogs(dp)
