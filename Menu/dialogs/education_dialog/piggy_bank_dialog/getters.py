from Connection.connection import song_api_connect
from aiogram_dialog import DialogManager


async def get_groups_game(**kwargs) -> dict:

    groups = await song_api_connect.send_request(
        url='/piggy_bank/groups',
        method='get')

    return {
        'data': groups,
        'count': len(groups)
    }


async def get_types_game(dialog_manager: DialogManager, **kwargs) -> dict:

    types_game = await song_api_connect.send_request(
        url='/piggy_bank/types_game',
        method='get')

    return {
        'data': types_game,
        'count': len(types_game)
    }


async def get_games_by_group_type(dialog_manager: DialogManager, **kwargs) -> dict:

    ctx = dialog_manager.current_context()

    games = await song_api_connect.send_request(
        url=f'/piggy_bank/games/?type_id={ctx.dialog_data.get("type_id")}&group_id={ctx.dialog_data.get("group_id")}',
        method='get')

    return {
        'data': games,
        'count': len(games)
    }


async def get_game(dialog_manager: DialogManager, **kwargs) -> dict:

    ctx = dialog_manager.current_context()

    file = await song_api_connect.send_request(
            url=f'/piggy_bank/games/{ctx.dialog_data.get("game_id")}/file',
            method='get_file'
    )

    ctx.dialog_data.update(file_path=file['file_path'])

    return {
        'game': await song_api_connect.send_request(
            url=f'/piggy_bank/games/{ctx.dialog_data.get("game_id")}',
            method='get'
        ),
        'file': file['file_path']
    }


async def get_legends_by_group(dialog_manager: DialogManager,  **kwargs) -> dict:

    ctx = dialog_manager.current_context()

    legends = await song_api_connect.send_request(
            url=f'/piggy_bank/legend/by_group/{ctx.dialog_data.get("group_id")}',
            method='get'
        )

    return {
        'data': legends,
        'count': len(legends)
    }


async def get_legend(dialog_manager: DialogManager, **kwargs) -> dict:

    ctx = dialog_manager.current_context()

    file = await song_api_connect.send_request(
        url=f'/piggy_bank/legends/{ctx.dialog_data.get("legend_id")}/file',
        method='get_file'
    )

    ctx.dialog_data.update(file_path=file['file_path'])

    return {
        'legend': await song_api_connect.send_request(
            url=f'/piggy_bank/legends/{ctx.dialog_data.get("legend_id")}',
            method='get'
        ),
        'file': file['file_path']
    }


async def get_ktd_by_group(dialog_manager: DialogManager, **kwargs) -> dict:

    ctx = dialog_manager.current_context()
    ktd = await song_api_connect.send_request(
            url=f'/piggy_bank/ktd/by_group/{ctx.dialog_data.get("group_id")}',
            method='get'
    )

    return {
        'data': ktd,
        'count': len(ktd)
    }


async def get_ktd(dialog_manager: DialogManager, **kwargs) -> dict:

    ctx = dialog_manager.current_context()

    file = await song_api_connect.send_request(
        url=f'/piggy_bank/ktd/{ctx.dialog_data.get("ktd_id")}/file',
        method='get_file'
    )

    ctx.dialog_data.update(file_path=file['file_path'])

    return {
        'ktd': await song_api_connect.send_request(
            url=f'/piggy_bank/ktd/{ctx.dialog_data.get("ktd_id")}',
            method='get'
        ),
        'file': file['file_path']
    }
