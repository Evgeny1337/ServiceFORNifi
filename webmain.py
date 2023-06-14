import aiohttp_jinja2
import jinja2
from aiohttp import web



fuck_data = {
    'USD': 75.0,
    'EUR': 90.0,
    'GBP': 105.0
}

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    request.app["sockets"].append(ws)
    try:
        async for _ in ws:
            pass
    finally:
        request.app['sockets'].remove(ws)
    return ws


async def index_post(request:web.Request):
    data = await request.json()
    for ws in request.app['sockets']:
        if not ws.closed:
            await ws.send_json(data)
    return web.Response(status=200)

async def index_handler(request):
    return aiohttp_jinja2.render_template('currency_table.html', request, context={'data': {}})


app = web.Application()
app["sockets"] = []

app.add_routes([
    web.get('/', index_handler),
    web.get('/ws', websocket_handler),
    web.post('/data',index_post)
])

aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader('templates')
)
web.run_app(app,host="127.0.0.1",port=8000)



