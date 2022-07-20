import sys
sys.path.insert(0, "...")

from base import BaseCli
from base.core.error_handler import _error
from pyrogram import filters
from pyrogram.types import Message
from db import *
from answers import answers
import re


@BaseCli.on_message(filters.me & (filters.regex('^(setlang (en|fa|انگلیسی|فارسی))$', re.I) | filters.regex('^(تنظیم زبان (en|fa|انگلیسی|فارسی))$', re.I)))
@BaseCli.on_edited_message(filters.me & (filters.regex('^(setlang (en|fa|انگلیسی|فارسی))$', re.I) | filters.regex('^(تنظیم زبان (en|fa|انگلیسی|فارسی))$', re.I)))
@_error
async def language(client: BaseCli, message: Message):
    language_for_set = re.search('(en|fa|انگلیسی|فارسی)', message.text).group(
        1).replace('فارسی', 'fa').replace('انگلیسی', 'en')
    language = get_language()

    if language == language_for_set:
        answer = answers['set_language_already']
        await message.edit(answer[language].format(language))
    else:
        set_language(language_for_set)
        answer = answers['language_changed']
        await message.edit(answer[language_for_set].format(language_for_set))
