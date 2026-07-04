import asyncio,aiohttp
from config import CHECK_INTERVAL
DEX_URL='https://api.dexscreener.com/token-profiles/latest/v1'
async def start_scanner():
    while True:
        async with aiohttp.ClientSession() as s:
            async with s.get(DEX_URL) as r:
                print(r.status)
        await asyncio.sleep(CHECK_INTERVAL)
