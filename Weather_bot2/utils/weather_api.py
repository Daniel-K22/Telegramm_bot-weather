import aiohttp
from config import WEATHER_API_KEY

async def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=74425b7990ea351eaf8725e5e01b7352&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                }
            else:
                raise Exception("Не удалось получить данные о погоде.")