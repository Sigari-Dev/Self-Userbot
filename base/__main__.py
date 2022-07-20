# Piniger UserBot
from . import BaseApi, BaseCli
from pyrogram import compose
import asyncio

async def main():
    apps = [
        BaseCli(),
        BaseApi(),
    ]
    await compose(apps)

if __name__ == "__main__":
    asyncio.run(main())