# Piniger UserBot
from . import BaseCli, BaseApi
from pyrogram import idle
import asyncio

async def main():
    cli = BaseCli()
    await cli.start()
    sudo = (await cli.get_me()).id
    await BaseApi(sudo).start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())