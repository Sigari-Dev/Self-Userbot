import sys

sys.path.insert(0, "...")

import re

from answers import answers
from base import BaseCli
from base.core import error, Message
from base.database import *
from pyrogram import filters


@BaseCli.on_message(filters.me & (filters.regex('^(setlang (en|fa|انگلیسی|فارسی))$', re.I) | filters.regex('^(تنظیم زبان (en|fa|انگلیسی|فارسی))$', re.I)))
@BaseCli.on_edited_message(filters.me & (filters.regex('^(setlang (en|fa|انگلیسی|فارسی))$', re.I) | filters.regex('^(تنظیم زبان (en|fa|انگلیسی|فارسی))$', re.I)))
@error
async def language(client: BaseCli, message: Message):
    language_for_set = re.search('(en|fa|انگلیسی|فارسی)', message.text).group(
        1).replace('فارسی', 'fa').replace('انگلیسی', 'en')
    language = message.language()

    if language == language_for_set:
        await message.edit(answers['set_language_already'][language].format(language))
    else:
        set_language(language_for_set)
        await message.edit(answers['language_changed'][language_for_set].format(language_for_set))
