# Got it from junks
# All in one code.

"""
Available Commands:
.tlol
.lol
.heart
.candy
.nothappy"""

from telethon import events
import asyncio
from collections import deque
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"candy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐ฆ๐ง๐ฉ๐ช๐๐ฐ๐ง๐ซ๐ฌ๐ญ"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"nothappy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐โน๏ธ๐โน๏ธ๐โน๏ธ๐"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"heart"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("โค๏ธ๐งก๐๐๐๐๐ค"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"ethink"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐ค๐ง๐คจ๐ค๐ง๐คจ"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"lol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("๐๐คฃ๐๐คฃ๐๐คฃ"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
