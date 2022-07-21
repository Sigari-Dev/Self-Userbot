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

DICE_EMOJI = ['🎲', 'تاس', 'dice']

@BaseCli.on_message(filters.me & filters.regex(f'^({"|".join(DICE_EMOJI)}) ([1-6])$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex(f'^({"|".join(DICE_EMOJI)}) ([1-6])$', re.I))
@error
async def dice(client: BaseCli, message: Message):
    language = get_language()
    answer = answers['dice']
    required_number = message.text.split()[1]
    await message.edit_text(answer[language].format(required_number))
    while True:
        msg = (await client.send_dice(message.chat.id, "🎲"))
        if msg.dice.value != int(required_number):
            await msg.delete()
        else:
            break