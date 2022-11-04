# For UniBorg
# By HunterX
# Syntax (.hl <link>)

from telethon import events
from hunterx.utils import admin_cmd
import asyncio
from telethon.tl import functions, types

@borg.on(admin_cmd(pattern="hl ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        input = event.pattern_match.group(1)
        await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
