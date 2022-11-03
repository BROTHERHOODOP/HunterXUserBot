# (c) @LOG_HME_PAPA_BOLTE
# Original written by @LOG_HME_PAPA_BOLTE edit by @export_gabbar

from telethon import events
import asyncio
from collections import deque
from hunterx.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"clock"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"))
	for _ in range(60):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
