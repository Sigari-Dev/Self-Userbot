import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pyrogram import Client

from config import *


class BaseCli(Client):
    def __init__(self):
        super().__init__(
            self.__class__.__name__.lower(),
            session_string= session_string if session_string else None,
            api_id=api_id,
            api_hash=api_hash,
            plugins=dict(root="base/plugins"),
            workdir="./",
            phone_number=phone_number
        )

class BaseApi(Client):
    def __init__(self):
        super().__init__(
            self.__class__.__name__.lower(),
            api_id=api_id,
            api_hash=api_hash,
            plugins=dict(root="base/plugins"),
            workdir="./",
            bot_token=bot_token
        )
