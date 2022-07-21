import sys
sys.path.insert(0, "...")

from base import BaseCli
from base.answers import answers
from base.core import error
from base.database import *
from pyrogram import filters
from pyrogram.types import Message
import re

@BaseCli.on_message(filters.me & filters.regex('^(ping|(ro)?bot|ر?بات|پینگ)$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex('^(ping|(ro)?bot|ر?بات|پینگ)$', re.I))
@error
async def ping(client: BaseCli, message: Message):
    language = get_language()
    answer = answers['ping']
    await message.edit(answer[language])
