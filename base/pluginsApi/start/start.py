import sys
sys.path.insert(0, "...")

from base import BaseApi
from base.core import error, symbolize
from pyrogram import filters
from pyrogram.types import Message
from db import *
from answers import answers
import re
from config import sudo_user

@BaseApi.on_message(filters.user(sudo_user) & filters.command("start"))
@error
async def start(client: BaseApi, message: Message):
    await message.reply(symbolize("Nothing important here"))
