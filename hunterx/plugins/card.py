# Original By 
# 
# 
# For #hunterx
#
# Card Generator
##############################
from faker import Faker as dc
from hunterx.utils import admin_cmd as hehe
from hunterx import bot as cobra
@cobra.on(hehe("card"))
async def _cobra(dark):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    danish = cyber.credit_card_full()
    await dark.edit(f"ℕ𝕒𝕞𝕖:-\n`{killer}`\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n`{kali}`\n\nℂ𝕒𝕣𝕕:-\n`{danish}`")
