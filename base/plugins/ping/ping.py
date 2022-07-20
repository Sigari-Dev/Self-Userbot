import sys
sys.path.insert(0, "...")

from base import Base
from base.core.error_handler import _error
from pyrogram import filters
from pyrogram.types import Message
from db import *
from answers import answers
import re

@Base.on_message(filters.me & filters.regex('^(ping|(ro)?bot|ر?بات|پینگ)$', re.I))
@Base.on_edited_message(filters.me & filters.regex('^(ping|(ro)?bot|ر?بات|پینگ)$', re.I))
@_error
async def ping(client: Base, message: Message):
    language = get_language()
    answer = answers['ping']
    if language == 'en':
        await message.edit(answer['en'])
    else:
        await message.edit(answer['fa'])
