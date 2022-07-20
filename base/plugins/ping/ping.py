from ... import Base
from ...core.error_handler import _error
from pyrogram import filters
from pyrogram.types import Message
from db import *
from answers import answers


@Base.on_message(filters.me & filters.regex('^([Pp][Ii][Nn][Gg]|([Rr][Oo])?[Bb][Oo][Tt]|ر?بات|پینگ)$'))
@_error
async def ping(client: Base, message: Message):
    language = get_language()
    answer = answers['ping']
    if language == 'en':
        await message.edit(answer['en'])
    else:
        await message.edit(answer['fa'])
