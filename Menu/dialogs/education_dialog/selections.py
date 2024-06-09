from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from state_fsm import EducationMenu

from typing import Any


async def on_section_select(callback: CallbackQuery,
                            widget: Any,
                            manager: DialogManager,
                            item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(section_id=item_id)

    await manager.switch_to(EducationMenu.chapters_choice)


async def on_chapter_select(callback: CallbackQuery,
                            widget: Any,
                            manager: DialogManager,
                            item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(chapter_id=item_id)

    await manager.switch_to(EducationMenu.chapter_view)