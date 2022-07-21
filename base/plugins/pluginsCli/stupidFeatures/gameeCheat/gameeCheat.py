import sys

sys.path.insert(0, "...")

import re

from answers import answers
from base import BaseCli
from base.core import Message, error
from base.database import *
from pyrogram import filters

from .gamee import set_score_gamee


@BaseCli.on_message(filters.me & (filters.regex('^(setscore (\d+) (.*))$', re.I) | filters.regex('^(تنظیم امتیاز (\d+) (.*))$')))
@BaseCli.on_edited_message(filters.me & (filters.regex('^(setscore (\d+) (.*))$', re.I) | filters.regex('^(تنظیم امتیاز (\d+) (.*))$')))
@error
async def gameeCheat(client: BaseCli, message: Message):
    # Later
    pass
