import time
from utils.weather_api import fetch_weather

CACHE = {}
CACHE_TIMEOUT = 3600  # 1 час

async def get_weather_from_cache_or_api(city):
    current_time = time.time()
    if city in CACHE and (current_time - CACHE[city]["timestamp"] < CACHE_TIMEOUT):
        return CACHE[city]["data"]
    data = await fetch_weather(city)
    CACHE[city] = {"data": data, "timestamp": current_time}
    return data
