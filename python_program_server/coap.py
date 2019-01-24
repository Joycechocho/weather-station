import asyncio

import aiocoap.resource as resource
import aiocoap


class BlockResource(resource.Resource):
   
    def __init__(self):
        super().__init__()
    
    def set_content(self, content):
        self.content = content

    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)
    
    async def render_put(self, request):
        print('PUT payload: %s' % request.payload)
        self.set_content(request.payload)
        return aiocoap.Message(payload=self.content)


def start_coap_test():
    root = resource.Site()
    root.add_resource(('.well-known', 'core'),
                      resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(('other', 'block'), BlockResource())
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('2601:281:8300:d314:a051:d135:5a9f:5a29', 5683)))
    asyncio.get_event_loop().run_forever()


