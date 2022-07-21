import sys

sys.path.insert(0, "...")

import os
import re

from base import BaseCli
from base.answers import answers
from base.core import Message, error
from base.database import *
from pyrogram import filters

DART_EMOJI = ["🎯", "دارت", "dart"]

@BaseCli.on_message(filters.me & filters.regex(f'^({"|".join(DART_EMOJI)}) (6)$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex(f'^({"|".join(DART_EMOJI)}) (6)$', re.I))
@error
async def dart(client: BaseCli, message: Message):
    #Later
    pass
