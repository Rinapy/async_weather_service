import aiohttp
import asyncio


from .settings import URL, TOKEN, DEFAULT_CORDS

all_data = []

async def get_weather(city: str, coord: str, session: aiohttp.ClientSession) -> dict:
    '''API async Requests.''' 
    
    url = URL.format(coord=coord, TOKEN=TOKEN)
    headers = {"accept": "application/json"}
    async with session.get(url=url, headers=headers) as response:
        data = [city, await response.json()]
        return data


async def load_weather_data(city_coord: dict[str: str]) -> dict:
    '''Weather dirty_dict loader.'''
    
    async with aiohttp.ClientSession() as session:
        tasks_request = []
        tasks_parsing = []
        clear_data = {}
        for city, coord in city_coord.items():
            task = asyncio.create_task(get_weather(city, coord, session))
            tasks_request.append(task)
        weather_lists = await asyncio.gather(*tasks_request)
        for list in weather_lists:
            task = asyncio.create_task(parsing(list))
            tasks_parsing.append(task)
        clear_data_list = await asyncio.gather(*tasks_parsing)
        for data in clear_data_list:
            clear_data.update(data)
        return clear_data


async def parsing(dirty_data: list[list, dict]) -> dict:
    try:
        value_list = dirty_data[1]['timelines']["minutely"]
    except KeyError:
        return {'func': 'parsing',
                'message': 'API Error'}
    temp_list = []
    for value in value_list:
        temp_list.append(value['values']['temperature'])
    return {dirty_data[0]: {'temperature': temp_list}}
    

def entry_point(coord):
    """Entry point for requests."""
    
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    clear_data = asyncio.run(load_weather_data(coord))
    return clear_data
