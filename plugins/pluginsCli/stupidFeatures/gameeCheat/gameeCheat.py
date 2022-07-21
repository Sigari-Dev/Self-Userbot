import sys
sys.path.insert(0, "...")

from base import BaseCli
from base.answers import answers
from base.core import error
from base.database import *
from base.libraries.gamee import set_score_gamee
from pyrogram import filters
from pyrogram.types import Message
import re

@BaseCli.on_message(filters.me & (filters.regex('^(setscore (\d+) (.*))$', re.I) | filters.regex('^(تنظیم امتیاز (\d+) (.*))$')))
@BaseCli.on_edited_message(filters.me & (filters.regex('^(setscore (\d+) (.*))$', re.I) | filters.regex('^(تنظیم امتیاز (\d+) (.*))$')))
@error
async def gameeCheat(client: BaseCli, message: Message):
    # Later
    pass