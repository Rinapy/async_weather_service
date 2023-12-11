import aiohttp
from aiohttp_jinja2 import template


@template('index.html')
async def index(request: dict) -> dict:
    '''Index view function'''
    return {'cities': ['Moscow', 'Ufa']}

async def integer(request: dict) -> dict:
    '''Index view function'''
    data = {
        'Moscow': {'temperature': (22, 33, 28, 33)},
        'Ufa': {'temperature':(24, 37, 22, 332)}}
    return aiohttp.web.json_response(data)