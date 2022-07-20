import sys
sys.path.insert(0, "...")

from base import BaseCli
from base.core import error as _error
from pyrogram import filters
from pyrogram.types import Message
from db import *
from answers import answers
import re
from gamee import set_score_gamee

@BaseCli.on_message(filters.me & (filters.regex('^(setscore (\d+) (.*))$', re.I) | filters.regex('^(تنظیم امتیاز (\d+) (.*))$')))
@BaseCli.on_edited_message(filters.me & (filters.regex('^(setscore (\d+) (.*))$', re.I) | filters.regex('^(تنظیم امتیاز (\d+) (.*))$')))
@_error
async def gameeCheat(client: BaseCli, message: Message):
    # Later
    pass