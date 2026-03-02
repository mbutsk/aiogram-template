import os

from dotenv import load_dotenv

from . import handlers
from .core import BotManager

load_dotenv()

token = os.getenv("BOT_TOKEN")

if token is None:
    raise ValueError("BOT_TOKEN environment variable not set")

mg = BotManager(token=token)

mg.load_routers()

bot = mg.bot
dp = mg.dp

__all__ = ["bot", "dp", "handlers"]
