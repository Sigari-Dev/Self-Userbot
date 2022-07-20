import sys
sys.path.insert(0, "...")

from base import BaseCli
from base.core.error_handler import _error
from pyrogram import filters
from pyrogram.types import Message
from db import *
from answers import answers
import re
import os

@BaseCli.on_message(filters.me & (filters.regex('^save$', re.I) | filters.regex('^ذخیره$', re.I)))
@BaseCli.on_edited_message(filters.me & (filters.regex('^save$', re.I) | filters.regex('^ذخیره$', re.I)))
@_error
async def saveExpirableMedia(client: BaseCli, message: Message):
    language = get_language()
    if replied := message.reply_to_message:
        if replied.media:
            answer = answers['start_downloading'][language]
            await message.edit(answer)
            filename = (await replied.download())
            await client.send_document("me", document=filename)
            os.remove(filename)
            answer = answers['downloaded'][language]
            await message.edit(answer)
        else:
            answer = answers['reply_on_media'][language]
            await message.edit(answer)
    else:
        answer = answers['reply_on_media'][language]
        await message.edit(answer)