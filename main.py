import asyncio
import logging

from aiogram.filters import Command, CommandObject
from aiogram import types

from aiogram_dialog import DialogManager, StartMode

from bot import bot, dp

from States_FSM import state_fsm


@dp.message(Command('start'))
async def start(message: types.Message, command: CommandObject):
    await message.answer('Добро пожаловать в бота!\n'
                         'Для вызова меню введи команду /get_menu.\n'
                         'Для поиска песни просто введи ее название.')


@dp.message(Command('get_menu'))
async def get_menu(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(state_fsm.MainMenu.main_menu, mode=StartMode.RESET_STACK)


async def main():

    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
