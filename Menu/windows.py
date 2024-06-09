from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Start
from aiogram_dialog.widgets.text import Const

from state_fsm import MainMenu, SongMenu, EducationMenu


# Главное окно
main_window = Window(
    Const('Главное меню'),
    Start(Const("Песни 🎵"), id="song_folder", state=SongMenu.category_type_choice),
    Start(Const("Метод папка 📁"), id="education_folder", state=EducationMenu.education_category_choice),
    Button(Const("Настройки ⚙️"), id="settings"),
    state=MainMenu.main_menu
)
