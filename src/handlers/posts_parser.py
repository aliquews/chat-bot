import json

from aiogram import Router
from aiogram.types import Message

from filters.chat_id import ChatIdFilter
from stats import CHANNEL_ID, POSTS_COUNT

router = Router()


@router.message(
    ChatIdFilter(chat_id=CHANNEL_ID),
)
async def increment_posts(message: Message):
    global POSTS_COUNT
    POSTS_COUNT = message.message_id
    # with open("data/stats.json", "w") as file:
    #     json.dump({"POSTS_COUNT": message.message_id}, file)
