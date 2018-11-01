import asyncio
from aiocoap import *
import time

class COAPClient(object):
    def __init__(self):
        self.ms = 0
        self.length = 0
        self.context = None
        asyncio.get_event_loop().run_until_complete(self.create_context())

    async def create_context(self):
        self.context = await Context.create_client_context()

    async def put(self, msg):
        self.ms = int(round(time.time()*1000))
        request = Message(code=PUT, payload=bytes(msg, 'utf-8'))
        request.opt.uri_host = '2601:281:8300:d314:a051:d135:5a9f:5a29'
        request.opt.uri_path = ("other", "block")
        response = await self.context.request(request).response
        self.ms = int(round(time.time()*1000))-self.ms
        self.length = len(response.payload.decode().split(','))
    
    def get_result(self):
        return [self.ms, self.length]

