import sys
sys.path.insert(0, "...")

from base import BaseApi
from base.answers import answers
from base.core import error
from base.utils import symbolize
from base.database import *
from pyrogram import filters
from pyrogram.types import Message
from config import sudo_user

@BaseApi.on_message(filters.user(sudo_user) & filters.command("start"))
@error
async def start(client: BaseApi, message: Message):
    await message.reply(symbolize("Nothing important here"))
