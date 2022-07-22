import sys

sys.path.insert(0, "...")

import os
import re

from base import BaseCli
from base.answers import answers
from base.core import Message, error
from base.database import *
from pyrogram import filters

DICE_EMOJI = ['🎲', 'تاس', 'dice']

@BaseCli.on_message(filters.me & filters.regex(f'^({"|".join(DICE_EMOJI)}) ([1-6])$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex(f'^({"|".join(DICE_EMOJI)}) ([1-6])$', re.I))
@error
async def dice(client: BaseCli, message: Message):
    language = message.language()
    required_number = message.text.split()[1]
    await message.edit_text(answers['dice'][language].format(required_number))
    while True:
        msg = (await client.send_dice(message.chat.id, "🎲"))
        if msg.dice.value != int(required_number):
            await msg.delete()
        else:
            break