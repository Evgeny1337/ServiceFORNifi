import asyncio
import random
from datetime import datetime
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def send_request():
    data = {
        'firstname':f'Userfirstname {random.randint(1, 100)}',
        'name': f'Username {random.randint(1, 100)}',
        'age': random.randint(18, 65),
        'email': f'user{random.randint(1, 100)}@example.com'
    }
    async with ClientSession() as session:
        async with session.post('http://localhost:8000/data', json=data) as response:
            print(f'{datetime.now()}: {response.status}')

scheduler = AsyncIOScheduler()
scheduler.add_job(send_request, 'interval', seconds=10)
scheduler.start()

try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass