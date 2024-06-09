import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Back, Select, ScrollingGroup, Column, Cancel, Button
from aiogram_dialog.widgets.text import Const, Format

from States_FSM.state_fsm import SongMenu

from . import selections, getters


# Окно выбора типа категории
category_type_choice = Window(
    Format('Выберите категорию'),
    Column(
        Select(
            Format('{item[name]}'),
            id='category_type_choice',
            item_id_getter=operator.itemgetter('id'),
            items='categories_type_list',
            on_click=selections.on_category_type_selected
        )
    ),
    Cancel(Const('<< В главное меню')),
    state=SongMenu.category_type_choice,
    getter=getters.get_type_categories
)


# Окно выбора категории выбранного типа
category_choice = Window(
    Const('Выберите подкатегорию'),
    ScrollingGroup(
        Select(
            Format('{item[category]}'),
            id='category_choice',
            item_id_getter=operator.itemgetter('id'),
            items='categories_by_type_list',
            on_click=selections.on_category_song_selected
        ),
        id='categories_list',
        hide_on_single_page=True,
        width=2,
        height=10,
    ),
    Back(Const('<< Назад')),
    Cancel(Const('<<< В главное меню')),
    getter=getters.get_category_by_type,
    state=SongMenu.category_choice
)


# Окно выбора песни
song_choice = Window(
    Const('Все что удалось найти'),
    ScrollingGroup(
        Select(
            Format('{item[title]}'),
            id='song_choice',
            item_id_getter=operator.itemgetter('id'),
            items='songs_by_category',
            on_click=selections.on_song_selected
        ),
        id='songs_by_category',
        hide_on_single_page=True,
        width=1,
        height=10,
    ),
    Back(Const('<< Назад')),
    Cancel(Const('<<< В главное меню')),
    getter=getters.get_songs_by_category,
    state=SongMenu.song_choice
)


# Показ самой песни
song_view = Window(
    Format('<b>{song[title]}</b>\n'),
    Format('{song[text]}'),
    Back(Const('<< Назад')),
    Cancel(Const('<<< В главное меню')),
    parse_mode='HTML',
    getter=getters.get_song_by_id,
    state=SongMenu.song_view
)
