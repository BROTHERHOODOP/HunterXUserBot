

    # original by @Rishi_krd
    # with Noob HUNTERX
    # Team HX
    # Keep Credits
    

from lyrics_extractor import SongLyrics as sl
import random, re
from hunterx import bot, CMD_HELP
from hunterx.utils import admin_cmd


@bot.on(admin_cmd(pattern=r"lyrics ?(.*)"))
async def original(event):
    if not event.pattern_match.group(1):
        await event.edit("give query to search.")
        return
    noob = event.pattern_match.group(1)
    await event.edit('```Getting lyrics..```')
    dc=(random.randrange(1,3))
    if hx==1:
       hunter = "AIzaSyAyDBsY3WRtB5YPC6aB_w8JAy6ZdXNc6FU"
    if hx==2: 
       hunter = "AIzaSyBF0zxLlYlPMp9xwMQqVKCQRq8DgdrLXsg"
    if hx==3:
       hunterx = "AIzaSyDdOKnwnPwVIQ_lbH5sYE4FoXjAKIQV0DQ"
    extract_lyrics = sl( f"{danish}", "15b9fb6193efd5d90")
    sh1vm = extract_lyrics.get_lyrics(f"{noob}")
    a7ul = sh1vm['lyrics'] 
    await event.client.send_message(event.chat_id, a7ul , reply_to=event.reply_to_msg_id)
    await event.delete()
    
    
