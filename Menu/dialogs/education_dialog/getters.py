from connection import song_api_connect
from aiogram_dialog import DialogManager


async def get_sections_methodical_book(dialog_manager: DialogManager, **kwargs) -> dict:
    sections = await song_api_connect.send_request(method='get', url='/methodical_book/sections/')

    return {
        "sections": sections,
        "count": len(sections)
    }


async def get_charpters_by_section(dialog_manager: DialogManager, **kwargs) -> dict:
    ctx = dialog_manager.current_context()
    chapters = await song_api_connect.send_request(method='get',
                                                   url=f'/methodical_book/sections/{ctx.dialog_data.get("section_id")}')

    return {
        "chapters": chapters,
        "count": len(chapters)
    }


async def get_chapter(dialog_manager: DialogManager, **kwargs) -> dict:
    ctx = dialog_manager.current_context()
    file = await song_api_connect.send_request(method='get_file',
                                               url=f'/methodical_book/chapters/file/{ctx.dialog_data.get("chapter_id")}')

    ctx.dialog_data.update(file_path=file['file_path'])

    return file
