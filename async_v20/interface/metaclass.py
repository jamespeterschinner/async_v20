import asyncio
class async_class(object):

    async def __ainit__(self, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__ainit__(*args, **kwargs))
