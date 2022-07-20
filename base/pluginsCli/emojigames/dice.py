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

DICE_EMOJI = ["🎲","تاس"]

@BaseCli.on_message(filters.me & filters.regex(f'^({DICE_EMOJI[0]}|tas|{DICE_EMOJI[1]}) ([1-6])$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex(f'^({DICE_EMOJI[0]}|tas|{DICE_EMOJI[1]}) ([1-6])$', re.I))
@error
async def dice(client: BaseCli, message: Message):
    language = get_language()
    answer1 = answers['dice']
    answer2 = answers['invalid_dice']
    required_number = message.text.split()[1]
    if 0 < int(required_number) < 7:
        await message.edit_text(answer1[language].format(required_number))
        while True:
            msg = await app.send_dice(message.chat.id, "🎲")
            if msg.dice.value != int(required_number):
                await msg.delete()
            else:
                break
    else:
        await message.edit_text(answer2[language])