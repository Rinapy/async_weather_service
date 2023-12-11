from .views import frontend
from aiohttp import web

def setup_routers(app: web.Application) -> None:
    '''Routers setup in app.'''
    
    app.add_routes([web.get('/', frontend.index), web.get('/integer', frontend.integer)])