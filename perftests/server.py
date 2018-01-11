from tests.fixtures.routes import routes
from tests.fixtures.server import rest_headers
from itertools import cycle
from perftests.account_changes_json import changes
import gzip
from aiohttp import web
import asyncio

routes.update({('GET', '/v3/accounts/123-123-1234567-123/changes'): cycle(changes)})

async def handler(request):
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')
    response = routes[(method, path)]
    json = response
    if not isinstance(json, str):
        json = next(response)
    return web.Response(body=gzip.compress(bytes(json, encoding='utf8')), headers=rest_headers,
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