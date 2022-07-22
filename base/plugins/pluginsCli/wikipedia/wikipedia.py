import sys

sys.path.insert(0, "...")

import os
import re

from base import BaseCli
from base.answers import answers
from base.core import Message, error
from base.database import *
from pyrogram import filters
from wikipedia import set_lang, summary

@BaseCli.on_message(filters.me & filters.regex(f'^(wikipedia|ویکی پدیا)', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex(f'^(wikipedia|ویکی پدیا)', re.I))
@error
async def wiki(client: BaseCli, message: Message):
    set_lang(message.language())
    result = summary("".join(message.text.split()[1::]))
    await message.edit_text(result)
