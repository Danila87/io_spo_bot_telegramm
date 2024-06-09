from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from state_fsm import SongMenu

from typing import Any


async def on_category_type_selected(callback: CallbackQuery,
                                    widget: Any,
                                    manager: DialogManager,
                                    item_id: str) -> None:
    ctx = manager.current_context()
    ctx.dialog_data.update(category_type_id=item_id)

    await manager.switch_to(SongMenu.category_choice)


async def on_category_song_selected(callback: CallbackQuery,
                                    widget: Any,
                                    manager: DialogManager,
                                    item_id: str) -> None:
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)

    await manager.switch_to(SongMenu.song_choice)


async def on_song_selected(callback: CallbackQuery,
                           widget: Any,
                           manager: DialogManager,
                           item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(song_id=item_id)

    await manager.switch_to(SongMenu.song_view)
