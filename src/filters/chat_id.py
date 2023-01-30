from typing import Union

from aiogram.filters.base import Filter
from aiogram.types import Message


class ChatIdFilter(Filter):
    
    def __init__(self, chat_id: Union[int, list[int]]) -> None:
        self.chat_id = chat_id

    async def __call__(self, message: Message):
        if isinstance(self.chat_id, int):
            return message.chat.id == self.chat_id
        else:
            return message.chat.id in self.chat_id