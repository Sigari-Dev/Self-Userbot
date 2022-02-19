# Self-Userbot
Userbot for telegram with pyrogram[Multi-plugin]

```
coming soon...
```

## Example plugin
```python
from base import WirexUser
from base.core import _error, is_admin
from pyrogram import Client, filters
from pyrogram.types import Message

__PLUGIN__ = "Test"

@WirexUser.on_message(filters.regex(r"^[Tt]est$") & is_admin("self"))
@_error
async def test(client: Client, update: Message):
    await update.edit("...")

```

## Channel:

©2022 - <a href=https://t.me/PiniGerTeam>PiniGerTeam™</a>
