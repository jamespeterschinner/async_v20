from tests.fixtures.routes import routes
from tests.fixtures.server import rest_headers
import gzip
from aiohttp import web
import asyncio

async def handler(request):
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')
    response = routes[(method, path)]
    return web.Response(body=gzip.compress(bytes(response, encoding='utf8')), headers=rest_headers,
                        status=200)
async def main(loop):
    await loop.create_server(web.Server(handler), "127.0.0.1", 8080)
    print("======= Serving on http://127.0.0.1:8080/ ======")
    await asyncio.sleep(100 * 3600)


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main(loop))
except KeyboardInterrupt:
    pass
loop.close()