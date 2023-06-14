from aiohttp import web




async def get_router(request:web.Request):
    data = await request.json()
    print(data)
    return web.json_response({"OK":"OK"})
    


app = web.Application()
app.router.add_post("/kek",get_router)
web.run_app(app,host="127.0.0.1",port=8000)




