import sys
sys.path.insert(0, "...")

from base import BaseCli
from base.core import error
from pyrogram import filters
from pyrogram.types import Message
from db import *
from answers import answers
import re
import os

DART_EMOJI = ["🎯", "دارت", "dart"]

@BaseCli.on_message(filters.me & filters.regex(f'^({"|".join(DART_EMOJI)}) (6)$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex(f'^({"|".join(DART_EMOJI)}) (6)$', re.I))
@error
async def dart(client: BaseCli, message: Message):
    #Later
    pass