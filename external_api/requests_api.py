import aiohttp
import asyncio

from settings import URL, TOKEN, DEFAULT_CORDS

all_data = []

async def get_weather(city: str,cords: str, session: aiohttp.ClientSession) -> dict:
    '''API async Requests.''' 
    url = URL.format(cords=cords, TOKEN=TOKEN)
    async with session.get(url) as response:
      all_data.append({city: await response.text()})
      return response


async def load_weather_data(city_cords: dict[str: str]) -> dict:
    '''Weather dict loader.'''
    async with aiohttp.ClientSession() as session:
        tasks = []
        for city, cords in city_cords.items():
            task = asyncio.create_task(get_weather(city, cords, session))
            tasks.append(task)
        await asyncio.gather(*tasks)
    return all_data

def start_requests(city_cords):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.run(load_weather_data(city_cords=city_cords))
