from aiohttp import web
from app.app import App
import asyncio

main = web.Application()

app = App()

main.router.add_route('POST', '/reg/', app.reg)
main.router.add_route('POST', '/auth/', app.auth)

web.run_app(main, host='0.0.0.0', port='8090')
