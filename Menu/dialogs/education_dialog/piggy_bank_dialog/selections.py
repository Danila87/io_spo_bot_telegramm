from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from state_fsm import PiggyBankMenu

from typing import Any


async def on_group_select(callback: CallbackQuery,
                               widget: Any,
                               manager: DialogManager,
                               item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(group_id=item_id)

    await manager.switch_to(PiggyBankMenu.category_choice)


async def on_type_game_select(callback: CallbackQuery,
                              widget: Any,
                              manager: DialogManager,
                              item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(type_id=item_id)

    await manager.switch_to(PiggyBankMenu.game_choice)


async def on_game_select(callback: CallbackQuery,
                         widget: Any,
                         manager: DialogManager,
                         item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(game_id=item_id)

    await manager.switch_to(PiggyBankMenu.game_show)


async def on_legend_select(callback: CallbackQuery,
                           widget: Any,
                           manager: DialogManager,
                           item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(legend_id=item_id)

    await manager.switch_to(PiggyBankMenu.legend_show)


async def on_ktd_select(callback: CallbackQuery,
                        widget: Any,
                        manager: DialogManager,
                        item_id: str) -> None:

    ctx = manager.current_context()
    ctx.dialog_data.update(ktd_id=item_id)

    await manager.switch_to(PiggyBankMenu.ktd_show)
