import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text

from handlers import commandsRouter
from filters.chat_type import ChatTypeFilter

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5917326295:AAG_sxuQ4DrEpOoP9tJx02uIAKnhwvZ9f9M")
dp = Dispatcher()


dp.message.filter(ChatTypeFilter(chat_type=['private', 'group', 'supergroup']))


async def main():
    dp.include_router(commandsRouter)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())