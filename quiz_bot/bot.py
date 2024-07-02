import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot

from quiz_bot.handlers import dp
from quiz_bot.db import create_table


logging.basicConfig(level=logging.INFO)

load_dotenv()
bot = Bot(token=os.getenv('BOT_API_TOKEN'))


async def main():
    await create_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
