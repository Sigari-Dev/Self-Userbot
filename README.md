<p align="center">
    <a href="https://github.com/Sigari-Dev/Self-Userbot">
        <img src="https://s5.imgcdn.dev/7JFyg.jpg" alt="PiniGerSelf">
    </a>
    <br>
    <b>Pluggable Telegram UserBot</b>
    <br>
</p>

# PiniGerSelf 🔥

![Python Version](https://img.shields.io/badge/python-3.8/3.9-lightgrey)
![Stars](https://img.shields.io/github/stars/Sigari-Dev/Self-Userbot)
![Forks](https://img.shields.io/github/forks/Sigari-Dev/Self-Userbot)
![Repo Size](https://img.shields.io/github/repo-size/Sigari-Dev/Self-Userbot)

> **PiniGerSelf** is a Powerful , Pluggable Telegram UserBot written in Python using [Pyrogram](https://github.com/pyrogram/pyrogram).

# Deploy to Vps

```
$ git clone https://github.com/Sigari-Dev/Self-Userbot.git
$ cd Self-Userbot
$ chmod +x install.sh
$ ./install.sh && pip install -r requirements.txt

Then edit config.py with your favorite text editor and save it!
run:
$ python -m base
```

## Example plugin
```python
from ... import Base
from pyrogram import filters
from pyrogram.types import Message

__PLUGIN__ = "Test"

@Base.on_message(filters.regex(r"^[Tt]est$") & filters.me)
async def test(client: Base, update: Message):
    await update.edit("...")

```

### Support & Discussions 👥
<a href="https://t.me/PiniGerSelf"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"> - [Channel 💬](https://t.me/PiniGerSelf),

<a href="https://t.me/PiniGerSelf_GP"><img src="https://img.shields.io/badge/Join-Group%20Support-blue.svg?style=for-the-badge&logo=Telegram"> - 
[Support ❤️](https://t.me/PiniGerSelf_GP) 

### Powered

> ©2022 - <a href=https://t.me/PiniGerTeam>PiniGerTeam™</a>
