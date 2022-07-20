import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import *
from pyrogram import Client

class Base(Client):
    def __init__(self):
        super().__init__(
            self.__class__.__name__.lower(),
            api_id=api_id,
            api_hash=api_hash,
            plugins=dict(root=f"{self.__class__.__name__.lower()}/plugins"),
            workdir="./",
        )
Base().run()