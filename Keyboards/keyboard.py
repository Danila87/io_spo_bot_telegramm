from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup, ButtonType, ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from typing import Optional

from abc import ABC, abstractmethod


class Keyboards(ABC):

    def __init__(self, keyboard_builder: [InlineKeyboardBuilder, ReplyKeyboardBuilder]):
        self.builder = keyboard_builder()

    def __call__(self):
        return self.builder.as_markup()

    @abstractmethod
    async def clear_builder(self):
        pass


####################################
#         Inline keyboards         #
####################################


class SongsCallback(CallbackData, prefix='songs'):
    action: str
    song_id: Optional[int] = None
    category_id: Optional[int] = None


class SongsCategoryCallback(CallbackData, prefix='songs_category'):
    action: str
    category_id: Optional[int] = None


class SongsInlineKeyboard(Keyboards):

    def __init__(self, song_list: list = None):

        super().__init__(keyboard_builder=InlineKeyboardBuilder)
        self.song_list = song_list

    def create_songs_keyboard(self):

        self.clear_builder()

        for song in self.song_list:
            self.builder.button(text=song['title_song'], callback_data=SongsCallback(
                action='get_song',
                song_id=song['id_song']))

        self.builder.adjust(1)

    def create_song_categories_keyboard(self):

        self.clear_builder()

        self.builder.button(text='По отрядам',
                            callback_data=SongsCategoryCallback(action='get_squads'))

        self.builder.button(text='Действующие/Недействующие',
                            callback_data=SongsCategoryCallback(action='get_active_inactive'))

        self.builder.button(text='Другое',
                            callback_data=SongsCategoryCallback(action='get_other_song'))

        self.builder.button(text='Удалить сообщение',
                            callback_data=SongsCategoryCallback(action='close'))

        self.builder.adjust(1)

    def category_builder(self, payload: list[dict]):

        self.clear_builder()

        for category in payload:
            self.builder.button(text=category['title_category'],
                                callback_data=SongsCallback(action='get_songs_by_category',
                                                            category_id=category['id']))

        self.builder.button(text='Назад',
                            callback_data=SongsCategoryCallback(action='back'))

        self.builder.adjust(1)

    def create_song_button(self):

        self.clear_builder()

        self.builder.button(text='Назад', callback_data=SongsCallback(
            action='back_song_list'
        ))
        self.builder.button(text='Закрыть', callback_data=SongsCallback(
            action='close'
        ))

        self.builder.adjust(1)

    def create_main_menu(self):
        self.clear_builder()

        self.builder.button(text='Песни', callback_data=SongsCallback(
            action='open_all_category_song'
        ))
        self.builder.button(text='Настройки', callback_data=SongsCallback(
            action='open_settings'
        ))

        self.builder.adjust(1)

    def clear_builder(self):

        self.builder = InlineKeyboardBuilder()


songs_keyboard = SongsInlineKeyboard()


####################################
#          Reply keyboards         #
####################################


class MainMenu(Keyboards):

    def __init__(self):

        super().__init__(keyboard_builder=ReplyKeyboardBuilder)
        self.create_main_menu()

    def __call__(self):
        return self.builder.as_markup(resize_keyboard=True)

    def create_main_menu(self):

        self.builder.add(KeyboardButton(text='Песни'))
        self.builder.add(KeyboardButton(text=''))

        self.builder.adjust(1)

    def clear_builder(self):
        self.builder = ReplyKeyboardBuilder()


reply_keyboard = MainMenu()
