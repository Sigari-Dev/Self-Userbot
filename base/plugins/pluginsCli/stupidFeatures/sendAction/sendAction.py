from pyrogram import filters
from base.database import *
from base.core import Message, error
from base.utils import get_by_language
from base import BaseCli
from answers import answers
import re
import sys

sys.path.insert(0, "...")


@BaseCli.on_message(filters.me & (filters.regex("setaction (all|custom|off|همه|خاموش|شخصی)") |filters.regex("ارسال اکشن (all|custom|off|همه|خاموش|شخصی)")))
@error
async def set_action(client: BaseCli, message: Message):
    language = message.language()
    action = message.text.lower().split(' ')[-1]
    action = action.replace(
        'همه', 'all'
    ).replace(
        'شخصی', 'custom'
    ).replace(
        'خاموش', 'off'
    )
    current_action = get_action_mode()

    if not action == current_action:
        set_action_mode(action)
        await message.edit(answers['action_mode_setted'][language].format(get_by_language(action, language)))
    else:
        await message.edit(answers['already_mode_type'][language].format(get_by_language(action, language)))

@BaseCli.on_message(filters.me & (filters.regex("setactiontype (all|custom|off|همه|خاموش|شخصی)") |filters.regex("ارسال اکشن (all|custom|off|همه|خاموش|شخصی)")))
@error
async def set_action(client: BaseCli, message: Message):
    pass
