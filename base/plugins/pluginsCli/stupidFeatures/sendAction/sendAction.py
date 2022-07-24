import sys

sys.path.insert(0, "...")

from pyrogram import filters
from pyrogram.enums import chat_action
from base.database import *
from base.core import Message, error
from base.utils import get_by_language
from base import BaseCli
from answers import answers
import re

@BaseCli.on_message(~filters.me)
async def do_action(client: BaseCli, message: Message):
    action_type = eval("chat_action.ChatAction." + get_action_type().upper())
    if get_action_mode() == 'all':
        await client.send_chat_action(message.chat.id, action_type)
    elif get_action_mode() == 'custom':
        if is_in_action_chats(message.chat.id):
            await client.send_chat_action(message.chat.id, action_type)


@BaseCli.on_message(filters.me & (filters.regex("setaction (all|custom|off|همه|خاموش|شخصی)", re.I) | filters.regex("ارسال اکشن (all|custom|off|همه|خاموش|شخصی)", re.I)))
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
        await message.edit(answers['already_action_type'][language].format(get_by_language(action, language)))


@BaseCli.on_message(filters.me & filters.regex("(setactiontype|نوع اکشن) (typing|upload_photo|record_video|record_voice|upload_document|choose_sticker|find_location|record_video_note|playing)"), re.I)
@error
async def set_type_action(client: BaseCli, message: Message):
    language = message.language()
    action_type = message.matches[0].group(2)
    current_action_type = get_action_type()

    if not action_type == current_action_type:
        set_action_type(action_type)
        await message.edit(answers['action_type_setted'][language].format(get_by_language(action_type, language)))
    else:
        await message.edit(answers['already_action_type'][language].format(get_by_language(action_type, language)))


@BaseCli.on_message(filters.me & filters.regex("(add action|rem action|اضافه اکشن|حذف اکشن)", re.I))
@error
async def action_custom(client: BaseCli, message: Message):
    language = message.language()

    is_added = is_in_action_chats(message.chat.id)
    match = message.matches[0].group(1)
    match = match.replace(
        'اضافه اکشن', 'add action'
    ).replace(
        'حذف اکشن', 'rem action'
    ).split(' ')
    add_rem = match[0]
    
    if add_rem == 'add':
        if not is_added:
            add_to_action_chats(message.chat.id)
            await message.edit(answers['added_to_action_chats'][language])
        else:
            await message.edit(answers['already_added_to_action_chats'][language])
    else:
        if is_added:
            remove_from_action_chats(message.chat.id)
            await message.edit(answers['removed_from_action_chats'][language])
        else:
            await message.edit(answers['already_removed_from_action_chats'][language])
