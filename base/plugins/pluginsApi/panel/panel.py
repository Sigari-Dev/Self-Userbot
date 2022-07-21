import sys

sys.path.insert(0, "...")

import re

from answers import answers
from base import BaseApi
from base.database import *
from base.utils import symbolize
from config import sudo_user
from pyrogram import filters
from pyrogram.types import InlineQuery


@BaseApi.on_inline_query(filters.user(sudo_user))
async def panel(client: BaseApi, update: InlineQuery):
    # Handle inline query here
    pass
