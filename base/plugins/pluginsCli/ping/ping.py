import sys

sys.path.insert(0, "...")

import os
import re

from answers import answers
from base import BaseCli
from base.core import Message, error
from base.database import *
from pyrogram import filters


@BaseCli.on_message(filters.me & filters.regex('^(ping|(ro)?bot|ر?بات|پینگ)$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex('^(ping|(ro)?bot|ر?بات|پینگ)$', re.I))
@error
async def ping(client: BaseCli, message: Message):
    language = message.language()
    await message.edit(answers['ping'][language])
