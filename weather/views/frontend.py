import aiohttp
from aiohttp_jinja2 import template
from external_api.requests_api import load_weather_data


@template('index.html')
async def index(request: dict) -> dict:
    '''Index view function'''
    return {'cities': ['Moscow', 'Ufa', 'St-Petersburg']}

async def integer(request: dict) -> dict:
    '''Index view function'''
    data = {
        'Moscow': {'temperature': (22, 33, 28, 33)},
        'Ufa': {'temperature':(24, 37, 22, 332)}}
    coords = {
        'Moscow': '55.7522,37.6156',
        'Ufa': '54.7431,55.9678',
        'St-Petersburg': '59.9386,30.3141'
    }
    
    data = await load_weather_data(coords)
    return aiohttp.web.json_response(data)