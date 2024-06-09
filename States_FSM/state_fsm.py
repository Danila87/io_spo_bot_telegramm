from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):

    main_menu = State()

    file_view = State()


class SongMenu(StatesGroup):

    category_type_choice = State()
    category_choice = State()
    song_choice = State()
    song_view = State()


class EducationMenu(StatesGroup):

    education_category_choice = State()
    sections_choice = State()
    chapters_choice = State()
    chapter_view = State()

    piggy_bank = State()


class PiggyBankMenu(StatesGroup):

    group_choice = State()
    category_choice = State()
    type_game_choice = State()
    game_choice = State()
    game_show = State()
    legend_choice = State()
    legend_show = State()
    ktd_choice = State()
    ktd_show = State()


class PiggyBankGames(StatesGroup):

    type_game_choice = State()
    game_choice = State()
    game_show = State()
