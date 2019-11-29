import asyncio
from motor.motor_asyncio import AsyncIOMotorClient


class Mongo_db:
    def __init__(self):
        self.db = AsyncIOMotorClient('mongodb://websocket_server_db:27017').test

    async def reg_user(self, login, password):
        result = await self.db.test_collection.insert_one({'login': login, 'password': password})
        return result.inserted_id

    async def user_auth(self, login, password):
        result = await self.db.test_collection.count_documents({'login': login, 'password': password})
        return result

    async def test_find(self):
        data = self.db.test_collection.find()
        return data.to_list(length=100)
