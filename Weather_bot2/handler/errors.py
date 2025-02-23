from aiogram import Router
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

router = Router()

@router.errors()
async def error_handler(message: Message, error: Exception):
    await message.answer(_("Произошла ошибка. Попробуйте позже."))