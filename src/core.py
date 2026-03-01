from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .handlers import routers


class BotManager:
    def __init__(self, token: str):
        self.token = token
        self.bot = Bot(
            token=self.token,
            default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
        )
        self.dp = Dispatcher()

    def load_routers(self):
        for router in routers:
            self.dp.include_router(router)
