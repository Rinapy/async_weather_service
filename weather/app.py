from aiohttp import web
import aiohttp_jinja2
import jinja2

from .routers import setup_routers

async def create_app() -> web.Application:
    '''Creation web app and set settings.'''
    
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader(
            'weather', 'templates'
        )
    )
    setup_routers(app)
    return app