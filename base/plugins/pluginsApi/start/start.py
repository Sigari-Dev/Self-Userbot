import sys

sys.path.insert(0, "...")

import re

from answers import answers
from base import BaseApi
from base.database import *
from base.utils import symbolize
from config import sudo_user
from pyrogram import filters
from pyrogram.types import Message


@BaseApi.on_message(filters.user(sudo_user) & filters.command("start"))
async def start(client: BaseApi, message: Message):
    await message.reply(symbolize("Nothing important here"))
