from userbot.utils import admin_cmd
from hunter import CMD_HELP
from hunter import bot


@borg.on(admin_cmd(pattern=r"hhi ?(.*)")) #initially made by @NOOB_GUY_OP
async def hhi(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "šŗ"
    b = giveVar[7:8]
    if not b:
        b = "āØ"
    await event.edit(
        f"{a}{b}{b}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{a}{a}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{a}{a}{a}\nāāāāāāāā"
    )
# later made by me
@borg.on(admin_cmd(pattern=r"gws ?(.*)"))
async def gws(event):
    giveVar = event.text
    '''m = giveVar[5:-1]
    if not m:'''
    m = " Get Well Soon ! "
    a = giveVar[-1:]
    if a=="s":
        a = "š¹"
    elif not a:
        a = "š¹"
    await event.edit(
        f"{a}{a}{a}{a}{a}{a}{a} \n{a} {m} {a}\n{a}{a}{a}{a}{a}{a}{a}"
    )
@borg.on(admin_cmd(pattern=r"hii ?(.*)"))
async def hii(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "šŗ"
    b = giveVar[7:8]
    if not b:
        b = "āØ"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{b}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}"
    )
@borg.on(admin_cmd(pattern=r"hlo ?(.*)"))
async def hlo(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "šŗ"
    b = giveVar[7:8]
    if not b:
        b = "āØ"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{a}{a}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{a}{a}{a}{b}{a}{a}{a}{a}{b}"
    )
@borg.on(admin_cmd(pattern=r"bye ?(.*)"))
async def bye(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "āØ"
    b = giveVar[7:8]
    if not b:
        b = "šŗ"
    await event.edit(
        f"{a}{b}{b}{a}{a}{b}{a}{a}{a}{b}{a}{b}{b}{b}{a}\n{a}{b}{a}{b}{a}{a}{b}{a}{b}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{a}{a}\n{a}{b}{a}{b}{a}{a}{a}{b}{a}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{b}{a}"
    )
CMD_HELP.update(
    {
        "customs": "__**PLUGIN NAME :** Custom animations__\
    \n\nš** CMD ā** `.hhi(emoji)(emoji)`\
    \n**USAGE   ā  **Try it yourself (put space ) \
    \n\nš** CMD ā** `.hhi(emoji)(emoji)`\
    \n**USAGE   ā  **Try it yourself (put space )\
    \n\nš** CMD ā** `.gws(emoji)`\
    \n**USAGE   ā  **Try it yourself (put space )\
    \n\nš** CMD ā** `.hlo(emoji)(emoji)`\
    \n**USAGE   ā  **Try it yourself (put space )\
    \n\nš** CMD ā** `.bye(emoji)(emoji)`\
    \n**USAGE   ā  **Try it yourself (put space )"
    }
)
