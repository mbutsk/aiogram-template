import asyncio
import logging
import os

from aiogram.methods.delete_webhook import DeleteWebhook
from dotenv import load_dotenv

from src import core

load_dotenv()

token = os.getenv("BOT_TOKEN")

if token is None:
    raise ValueError("BOT_TOKEN environment variable not set")

mg = core.BotManager(token=token)

bot = mg.bot
dp = mg.dp


async def main() -> None:
    await bot(DeleteWebhook(drop_pending_updates=True))
    logging.basicConfig(level=logging.INFO)
    mg.load_routers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
