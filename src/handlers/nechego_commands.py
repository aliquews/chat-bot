import random
import numpy as np

from aiogram import Router, Bot
from aiogram.filters import Text, Command
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

from stats import CHANNEL_ID, BUFFER_CHAT_ID, POSTS_COUNT


router = Router()

@router.message(
    Command(commands=["pic"])
    #Text(startswith="!пик")
)
async def send_pic(message: Message, bot: Bot):
    global POSTS_COUNT
    random_id = np.random.randint(low=0, high=POSTS_COUNT)
    #random_id = random.randint(0, POSTS_COUNT)
    try:
        rand_message: Message = await bot.forward_message(chat_id=BUFFER_CHAT_ID, from_chat_id=CHANNEL_ID, message_id=random_id)
    except TelegramBadRequest:
        await send_pic(message, bot)
        return
    if rand_message.photo:
        await bot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=random_id)
    else:
        await bot.delete_message(chat_id=BUFFER_CHAT_ID, message_id=rand_message.message_id)
        await send_pic(message, bot)

@router.message(
    Command(commands=["info"])
    #Text(startswith="!инфа"),
)
async def answer_info_rand(message: Message):
    text = message.text.split('/info', maxsplit=1)
    print(text)
    await message.answer(f'я думаю что {text[1].replace(" ","", 1)} с вероятностью {random.randint(0, 100)}%')

# @router.message(
#     Text(text="!id")
# )
# async def get_id_message(message: Message):
#     await message.answer(f"message id is: {message.message_id}, chatid is: {message.chat.id}")
