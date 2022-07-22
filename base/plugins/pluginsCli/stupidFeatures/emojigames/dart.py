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

@BaseCli.on_message(filters.me & filters.regex(f'^({"|".join(DART_EMOJI)}) (hit)$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex(f'^({"|".join(DART_EMOJI)}) (hit)$', re.I))
@error
async def dart(client: BaseCli, message: Message):
    language = message.language()
    while True:
        msg = (await client.send_dice(message.chat.id, "🎯"))
        if msg.dice.value != 6:
            await msg.delete()
        else:
            await message.edit_text(answers['dart'][language])
            break