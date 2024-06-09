from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from Connection.connection import song_api_connect as song_api
from Keyboards.keyboard import songs_keyboard, SongsCallback

song_router = Router()


@song_router.message(F.text == 'Песни')
async def show_categories_songs(message: Message):

    songs_keyboard.create_song_categories_keyboard()
    await message.answer(text='Выберите категорию', reply_markup=songs_keyboard())


@song_router.message(F.text)
async def search_song_by_title(message: Message):

    """
    Поиск песни по названию
    """

    data = {
        "telegram_id": 1,
        "song_title": message.text
    }

    response = await song_api.send_request(method='post', url='/song/songs/search_title', data=data)

    if response:
        songs_keyboard.song_list = response
        songs_keyboard.create_songs_keyboard()

        await message.answer(text='Все что удалось найти', reply_markup=songs_keyboard())

        return

    await message.answer(text='Ничего не нашел')


@song_router.callback_query(SongsCallback.filter())
async def callback_song(callback: CallbackQuery, callback_data: SongsCallback):

    """
    Callback ловушка для песен
    """

    if callback_data.action == 'get_song':
        song = await song_api.send_request(url=f'/song/{callback_data.song_id}', method='get')

        songs_keyboard.create_song_button()
        await callback.message.edit_text(text=f'{html.bold(song["title"])}\n{song["text"]}',
                                         reply_markup=songs_keyboard(),
                                         parse_mode=ParseMode.HTML)

    if callback_data.action == 'back_song_list':
        songs_keyboard.create_songs_keyboard()
        await callback.message.edit_text(text='Все что удалось найти', reply_markup=songs_keyboard())

    if callback_data.action == 'close':
        await callback.message.delete()

    await callback.answer(show_alert=True)
