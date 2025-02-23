from aiogram import Router
from aiogram.types import Message
from utils.cache import get_weather_from_cache_or_api
from aiogram.utils.i18n import gettext as _

router = Router()

@router.message()
async def weather_handler(message: Message):
    city = message.text.strip()
    try:
        weather_data = await get_weather_from_cache_or_api(city)
        await message.answer(format_weather_message(weather_data))
    except Exception as e:
        await message.answer(_("Ошибка: {error}").format(error=str(e)))

def format_weather_message(data):
    return _(
        "Погода в {city}:\nТемпература: {temp}°C\nСостояние: {description}"
    ).format(city=data["city"], temp=data["temp"], description=data["description"])
