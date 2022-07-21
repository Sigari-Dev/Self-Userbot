import sys

sys.path.insert(0, "...")
import asyncio
import os
import re

from base import BaseCli
from base.answers import answers
from base.core import Message, error
from pyrogram import filters


async def run_command(*args):
    process = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return stdout

@BaseCli.on_message(filters.me & filters.regex('^(update|اپدیت)$', re.I))
@BaseCli.on_edited_message(filters.me & filters.regex('^(update|اپدیت)$', re.I))
@error
async def update(client: BaseCli, message: Message):
    language = message.language()
    _msg = await message.edit(answers['check_update'][language])
    commands = ["git", "pull"]
    stdout = await run_command(*commands)
    if "Already up to date." in stdout.decode():
        return await _msg.edit(answers['already_update'][language])
    await _msg.edit(answers['update'][language])
    os.execl(sys.executable, sys.executable, "-m", "base")
