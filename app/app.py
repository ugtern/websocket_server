from aiohttp import web
from app.databases import Mongo_db
from jose import jwt
import json


class App:
    def __init__(self):
        self.db = ''

    async def auth(self, req):

        body = await self.get_req_params(req)
        login = body.get('login')
        password = body.get('password')

        user = Mongo_db()
        result = await user.user_auth(login, password)
        if result > 0:
            token = jwt.encode({'client': login+password}, 'secret', algorithm='HS256')

            return web.json_response(status=200, data={'token': token}, headers={
                'Access-Control-Allow-Origin': req.headers['Origin']
                })

        return web.Response(status=500, text='error')

    async def reg(self, req):

        body = await self.get_req_params(req)
        login = body.get('login')
        password = body.get('password')

        user = Mongo_db()
        try:
            test = await user.reg_user(login=login, password=password)
        except:
            return web.Response(status=500, text="can't create user")

        print(test)

        return web.Response(status=200, text='user was registration')

    @staticmethod
    async def get_req_params(req):

        body = await req.read()
        body = json.loads(body.decode('utf-8'))

        return body
