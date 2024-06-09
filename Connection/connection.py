import aiohttp
import datetime
from typing import Literal


class Connection:
    METHODS = Literal['get', 'post', 'put', 'delete', 'get_file']

    def __init__(self, host: str, port: int):

        self.host = host
        self.port = port
        self.main_url = f'{host}:{port}'

    async def send_request(self, url: str, method: METHODS, data: dict = None) -> dict | list[dict]:

        async with aiohttp.ClientSession() as session:
            if method == 'get':
                async with session.get(self.main_url + url) as response:
                    return await response.json()

            if method == 'post':
                async with session.post(self.main_url+url, json=data) as response:
                    return await response.json()

            if method == 'get_file':
                async with session.get(self.main_url+url) as response:

                    filename = f'{datetime.datetime.now()}{response.headers.get("file_type")}'

                    with open(f'temp/{filename}', 'wb') as file:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            file.write(chunk)
                return {
                    'file_path': f'temp/{filename}'
                }


song_api_connect = Connection(host='http://127.0.0.1', port=8000)
