import sys
sys.path.insert(0, "...")

from base import BaseApi
from base.core import error, symbolize
from pyrogram import filters
from pyrogram.types import InlineQuery
from db import *
from answers import answers
import re
from config import sudo_user

@BaseApi.on_inline_query(filters.user(sudo_user))
@error
async def panel(client: BaseApi, update: InlineQuery):
    # Handle inline query here
    pass