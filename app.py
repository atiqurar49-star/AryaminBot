import asyncio
from bot.solana_scanner import start_scanner
async def main():
    await start_scanner()
if __name__=='__main__':
    asyncio.run(main())
