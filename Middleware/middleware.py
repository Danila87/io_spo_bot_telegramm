from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Message
from typing import Callable, Dict, Awaitable, Any
from Connection.connection import song_api_connect as song_api

NOT_REMOTE_COMMANDS: list[str] = ['/start', '/getMenuTest']


class CheckUserRegistration(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:

        payload = {
                  "telegram_id": data['event_from_user'].id,
                  "first_name": data['event_from_user'].first_name,
                  "last_name": data['event_from_user'].last_name,
                  "nickname": data['event_from_user'].username
                }
        await song_api.send_request(url='/service/check_user', data=payload, method='post')

        if hasattr(event, 'message') and event.message is not None and event.event.text not in NOT_REMOTE_COMMANDS:
            await event.message.delete()

        return await handler(event, data)


class Mute(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
            mute: int = 5
    ) -> Any:

        return await handler(event, data)
