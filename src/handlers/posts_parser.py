import json

from aiogram import Router
from aiogram.types import Message

from filters.chat_id import ChatIdFilter
from stats import CHANNEL_ID

router = Router()


@router.message(
    ChatIdFilter(chat_id=CHANNEL_ID),
)
async def increment_posts(message: Message):
    with open("data/stats.json", "w") as file:
        json.dump({"POSTS_COUNT": message.message_id}, file)
