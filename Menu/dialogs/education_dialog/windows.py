import operator
import os

from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Back, Select, ScrollingGroup, Cancel, Start
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.media import StaticMedia

from aiogram.types import CallbackQuery, ContentType

from state_fsm import EducationMenu, PiggyBankMenu

from . import getters, selections


async def go_sections_methodical_book(callback: CallbackQuery,
                                      button: Button,
                                      manager: DialogManager) -> None:

    await manager.switch_to(EducationMenu.sections_choice)


async def clear_file(callback: CallbackQuery,
                     button: Button,
                     manager: DialogManager) -> None:
    file_path = manager.dialog_data.get('file_path')
    os.remove(file_path)


education_choice_category = Window(
    Const('Выберите категорию'),
    Button(Const('Методичка 📔'), id='education_book', on_click=go_sections_methodical_book),
    Start(Const('Копилка 🐷'), id='piggy_bank', state=PiggyBankMenu.group_choice),
    Cancel(Const('<< Назад')),
    state=EducationMenu.education_category_choice
)

methodical_book_section_choice = Window(

    Const('Выберите раздел'),

    ScrollingGroup(

        Select(
            Format('{item[title]}'),
            id='section_choice',
            item_id_getter=operator.itemgetter('id'),
            items='sections',
            on_click=selections.on_section_select
        ),

        id='education_section_choice',
        hide_on_single_page=True,
        width=1,
        height=5

    ),

    Back(Const('<< Назад')),
    Cancel(Const('<<< В главное меню')),

    getter=getters.get_sections_methodical_book,
    state=EducationMenu.sections_choice

)

methodical_book_chapter_choice = Window(
    Const('Выберите тему'),

    ScrollingGroup(

        Select(
            Format('{item[title]}'),
            id='chapter_choice',
            item_id_getter=operator.itemgetter('id'),
            items='chapters',
            on_click=selections.on_chapter_select
        ),

        id='education_chapter_choice',
        hide_on_single_page=True,
        width=1,
        height=10

    ),

    Back(Const('<< Назад')),
    Cancel(Const('<<< В главное меню')),

    getter=getters.get_charpters_by_section,
    state=EducationMenu.chapters_choice
)

chapter_show = Window(
    Format('История ИО СПО'),
    StaticMedia(path=Format('{file_path}'), type=ContentType.DOCUMENT),
    Back(Const('<< Назад'), on_click=clear_file),
    Cancel(Const('<<< В главное меню')),
    state=EducationMenu.chapter_view,
    getter=getters.get_chapter
)
