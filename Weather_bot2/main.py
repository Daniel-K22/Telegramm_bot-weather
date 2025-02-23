from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.i18n import I18n

from config import TOKEN
from handlers import start, weather, errors

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Настройка локализации
i18n = I18n(path="locales", default_locale="en", domain="bot")
_ = i18n.gettext

# Регистрация хендлеров
dp.include_router(start.router)
dp.include_router(weather.router)
dp.include_router(errors.router)

if name == "__main__":
    dp.run_polling(bot)
