from Connection.connection import song_api_connect
from aiogram_dialog import DialogManager


async def get_type_categories(**kwargs) -> dict:
    type_categories = await song_api_connect.send_request(method='get',
                                                          url='/song/categories/type_categories/all')
    return {
        "categories_type_list": sorted(type_categories, key=lambda x: x['name']),
        "count": len(type_categories)
    }


async def get_category_by_type(dialog_manager: DialogManager, **kwargs) -> dict:
    ctx = dialog_manager.current_context()

    categories_by_type = await song_api_connect.send_request(method='get',
                                                             url=f'/song/type_category/{ctx.dialog_data.get("category_type_id")}')

    return {
        "categories_by_type_list": sorted(categories_by_type, key=lambda x: x['category']),
        "count": len(categories_by_type)
    }


async def get_songs_by_category(dialog_manager: DialogManager, **kwargs) -> dict:
    ctx = dialog_manager.current_context()

    songs_by_category = await song_api_connect.send_request(method='get',
                                                            url=f'/song/by_category/{ctx.dialog_data.get("category_id")}')
    songs_by_category = sorted(songs_by_category, key=lambda x: x['title'])

    return {
        "songs_by_category": songs_by_category,
        "count": len(songs_by_category)
    }


async def get_song_by_id(dialog_manager: DialogManager, **kwargs) -> dict:
    ctx = dialog_manager.current_context()

    return {
        "song": await song_api_connect.send_request(method='get', url=f'/song/{ctx.dialog_data.get("song_id")}')
    }