from aiogram import types
from aiogram.filters import BaseFilter


class PapayaFilter(BaseFilter):
    def __init__(self, text: str):
        # self.text: str = text.lower()
        pass

    async def __call__(self, message: types.Message) -> bool:
        if not message.text:
            return False
        return message.text.split()[-2].lower() == "папайя"
