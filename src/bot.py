import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import commandsRouter
from filters.chat_type import ChatTypeFilter

from load import TELEGRAM_API
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API)
dp = Dispatcher()


# dp.message.filter(ChatTypeFilter(chat_type=['private', 'group', 'supergroup']))


async def main():
    dp.include_router(commandsRouter)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())