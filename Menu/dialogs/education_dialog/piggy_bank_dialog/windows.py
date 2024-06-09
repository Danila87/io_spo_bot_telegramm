import operator
import os

from aiogram.types import CallbackQuery, ContentType

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Back, Select, ScrollingGroup, Cancel, Button, SwitchTo
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.media import StaticMedia

from state_fsm import PiggyBankMenu

from . import selections, getters


async def clear_file(callback: CallbackQuery,
                     button: Button,
                     manager: DialogManager) -> None:
    file_path = manager.dialog_data.get('file_path')
    os.remove(file_path)


async def go_legends(callback: CallbackQuery,
                     button: Button,
                     manager: DialogManager) -> None:
    await manager.switch_to(PiggyBankMenu.legend_choice)


async def go_ktd(callback: CallbackQuery,
                 button: Button,
                 manager: DialogManager) -> None:
    await manager.switch_to(PiggyBankMenu.ktd_choice)


async def go_games(callback: CallbackQuery,
                   button: Button,
                   manager: DialogManager) -> None:

    await manager.switch_to(PiggyBankMenu.type_game_choice)


def create_list_menu(title, getter, selection, back_state, state, *args) -> Window:
    return Window(
        Const(title),

        ScrollingGroup(

            Select(
                Format('{item[title]}'),
                id='piggy_list',
                item_id_getter=operator.itemgetter('id'),
                items='data',
                on_click=selection
            ),

            id='list_choice',
            height=10,
            width=2,
            hide_on_single_page=True
        ),
        SwitchTo(Const('<< Назад'), id='back', state=back_state),
        getter=getter,
        state=state,
        *args,
    )


def create_show_with_file(state, getter, back_state, *args) -> Window:
    return Window(

        *args,

        StaticMedia(path=Format('{file}'), type=ContentType.DOCUMENT),
        SwitchTo(Const('<< Назад'), id='back', state=back_state, on_click=clear_file),
        Cancel(Const('<<< В главное меню')),
        state=state,
        getter=getter,
        parse_mode='HTML'

    )


category_choice = Window(
    Const('Выберите категорию'),
    Button(Const('Игры'), id='games', on_click=go_games),
    Button(Const('КТД'), id='ktd', on_click=go_ktd),
    Button(Const('Легенды'), id='legends', on_click=go_legends),
    Back(Const('<< Назад')),
    state=PiggyBankMenu.category_choice
)


group_choice = Window(
    Const('Выберите категорию детей'),

    ScrollingGroup(

        Select(
            Format('{item[title]}'),
            id='group_choice',
            item_id_getter=operator.itemgetter('id'),
            items='data',
            on_click=selections.on_group_select
        ),

        id='group_game_choice',
        width=1,
        height=5,
        hide_on_single_page=True

    ),

    Cancel(Const('<< Назад')),
    getter=getters.get_groups_game,
    state=PiggyBankMenu.group_choice
)


type_game_choice = create_list_menu(
    title='Выберите тип игры',
    getter=getters.get_types_game,
    selection=selections.on_type_game_select,
    back_state=PiggyBankMenu.category_choice,
    state=PiggyBankMenu.type_game_choice
)


game_choice = create_list_menu(
    title='Выберите игру',
    getter=getters.get_games_by_group_type,
    selection=selections.on_game_select,
    back_state=PiggyBankMenu.type_game_choice,
    state=PiggyBankMenu.game_choice,
)

legend_choice = create_list_menu(
    title='Выберите легенду',
    getter=getters.get_legends_by_group,
    selection=selections.on_legend_select,
    back_state=PiggyBankMenu.category_choice,
    state=PiggyBankMenu.legend_choice,
)

ktd_choice = create_list_menu(
    title='Выберите КТД',
    getter=getters.get_ktd_by_group,
    selection=selections.on_ktd_select,
    back_state=PiggyBankMenu.category_choice,
    state=PiggyBankMenu.ktd_choice,
)

game_show = create_show_with_file(
    PiggyBankMenu.game_show,
    getters.get_game,
    PiggyBankMenu.game_choice,
    Format('<b>{game[title]}</b>\n'),
    Format('{game[description]}')
)

legend_show = create_show_with_file(
    PiggyBankMenu.legend_show,
    getters.get_legend,
    PiggyBankMenu.legend_choice,
    Format('<b>{legend[title]}</b>\n'),
    Format('{legend[description]}')
)

ktd_show = create_show_with_file(
    PiggyBankMenu.ktd_show,
    getters.get_ktd,
    PiggyBankMenu.ktd_choice,
    Format('<b>{ktd[title]}</b>\n'),
    Format('{ktd[description]}')
)