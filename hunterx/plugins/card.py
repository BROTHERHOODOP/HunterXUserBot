# Original By 
# 
# 
# For #hunterx
#
# Card Generator
##############################
from faker import Faker as dc
from hunterx.utils import admin_cmd as hehe
from hunterx import bot as hunter
@hunter.on(hehe("card"))
async def _hunter(dark):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    danish = cyber.credit_card_full()
    await dark.edit(f"βπππ:-\n`{killer}`\n\nπΈπππ£ππ€π€:-\n`{kali}`\n\nβππ£π:-\n`{danish}`")
