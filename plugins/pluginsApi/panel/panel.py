import sys
sys.path.insert(0, "...")

from base import BaseApi
from base.answers import answers
from base.core import error
from base.database import *
from pyrogram import filters
from pyrogram.types import InlineQuery
from config import sudo_user

@BaseApi.on_inline_query(filters.user(sudo_user))
@error
async def panel(client: BaseApi, update: InlineQuery):
    # Handle inline query here
    pass