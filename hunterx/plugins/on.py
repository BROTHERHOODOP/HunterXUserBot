# Thanks to @Rishi_krd Bro
# Thanks to Gabbar .. 
# Idea by HUNTERX
# Made by HUNTERX ....TEAM HX
# Kang with credits else gay...
# inline alive
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from hunterx.utils import admin_cmd
from hunterx import ALIVE_NAME, Lastupdate
from . import dcdef
from userbot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
        dc_text=(f"** π³π°ππΊ π²πΎπ±ππ° πΈπ πΎπ½π»πΈπ½π΄**\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\nβ About My System β\n\nβΎ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄Κκ±Ιͺα΄Ι΄** β {version.__version__}\nβΎ **κ±α΄α΄α΄α΄Κα΄ α΄Κα΄Ι΄Ι΄α΄Κ** β [α΄α΄ΙͺΙ΄](https://t.me/Dark_cobra_support)\nβΎ **ΚΙͺα΄α΄Ι΄κ±α΄**  β [ππππ’ πΏπΎ](https://github.com/DARK-COBRA)\nβΎ **α΄α΄α΄ΚΚΙͺΙ’Κα΄ ΚΚ** β [πΏππ§π -πΎπ€ππ§π](https://github.com/DARK-COBRA/DARKCOBRA)\n\nβΎ **α΄α΄α΄Ιͺα΄α΄** β {uptime}\n\nβΎ **α΄Κ α΄α΄sα΄α΄Κ** β [{DEFAULTUSER}](tg://user?id={ok})\n")
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/DARK-COBRA/DARKCOBRA"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/DARK-COBRA/DARKCOBRA/blob/master")],
                    [Button.url("String", "https://repl.it/@Danish00/DarkCobra#main.py"),
                    Button.url("Channel", "https://t.me/Dark_cobra_support"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="DARK Cobra",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="Dark Cobra",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)
