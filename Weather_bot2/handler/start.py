from aiogram import Router
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

router = Router()

@router.message(commands=["start"])
async def start_command(message: Message):
    await message.answer(_("Привет! Я погодный бот. Напиши название города, чтобы узнать погоду."))