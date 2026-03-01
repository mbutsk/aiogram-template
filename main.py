import asyncio
import logging

from aiogram.methods.delete_webhook import DeleteWebhook

from src import bot, dp


async def main() -> None:
    await bot(DeleteWebhook(drop_pending_updates=True))
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
