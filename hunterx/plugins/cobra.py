# hunterx Original ๐๐๐๐๐๐๐๐๐๐๐๐
# kangers Keep Credits ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐
# Made by fuck 
# Don't remove these lines u fool ,,, 
#
#
#hehehhe
#Making The Back Command Was The Toughest Work #by hunterx,rishi, programmer,hunter also v changed Pop up or inline help to text
#A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara 
#Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
# aur  unload load back close open kang kara ya idea bhi le to credit dena pehli 6 line nahi to bhut bura hoga tumara sath
from math import ceil
import asyncio
import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from hunterx import CMD_LIST, CMD_HELP
import io
#ABEE O KANGAR  BACK OPEN CLSE BTN KANG KIYA TO YE LONE CHIPKA DENA AUR GLOBALS K BINA NAHI CHALAGA aur global 5 gaja diff name and manipulation se imported hai 
#Making The Back Command Was The Toughest Work #by also v changed Pop up or inline help to text
from hunterx.utils import remove_plugin,load_module
#Making The Back Command Was The Toughest Work #by  also v changed Pop up or inline help to text
#A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara 
#Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

# ๐ฆโ๐ฆโ๐ตโ    ๐พโ๐ฆโ๐ญโ๐ฆโ   ๐ฆโ๐ฆโ๐พโ๐ชโ   ๐ฐโ๐ฎโ๐ธโ    ๐ฑโ๐ฎโ๐พโ๐ชโ??

# ๐จโ๐ญโ๐ฆโ๐ฑโ๐ดโ     ๐ธโ๐ฎโ๐ทโ   ๐ตโ๐ฑโ๐ชโ๐ฆโ๐ธโ๐ชโ   ๐ฌโ๐ชโ๐นโ๐ดโ๐บโ๐นโ   



    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
   
    async def opner(event):
            if event.query.user_id == bot.uid :
                current_page_number=0
                dc = paginate_help(current_page_number, CMD_LIST, "helpme")
                await event.edit("`>>>\n\nReopened The Main Menu of \nยฉhunterx` ", buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot,for more info visit @HunterXUserBot_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
       
  #       ๐ฎโ๐นโ๐ณโ๐ฆโ   ๐ฐโ๐พโ๐บโ  ๐ธโ๐ตโ๐พโ    ๐ฐโ๐ทโ   ๐ทโ๐ญโ๐ชโ    ๐ญโ๐ดโ     ๐ธโ๐ญโ๐ฆโ๐ฆโ๐ฉโ๐ฎโ   ๐ฐโ๐ทโ๐ณโ๐ฎโ   ๐ญโ   ๐ฐโ๐พโ๐ฆโ  ๐งโ๐ธโ๐ฉโ๐ฐโ

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            dc = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article("ยฉ Dark Cobra Userbot Help",text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),buttons=dc,link_preview=False)
            await event.answer([result] if result else None)
        else:
              reply_pop_up_alert = "Please get your own Userbot๐๐,for more info visit @DARK_COBRA_SUPPORT! ๐๐"
              await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))#hehe
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
          
            await event.edit(buttons=dc)
        else:
            Cobra = "Please get your own Userbot, and don't use mine for more info visit @HunterXUserBot_SUPPORT!"
            await event.answer(jay, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            
            await event.edit(buttons=dc)
        else:
              TheDark = "Please get your own Userbot๐๐,for more info visit @DARK_COBRA_SUPPORT! ๐๐"
              await event.answer(TheDark, cache_time=0, alert=True)
 #hehehehehhehhehhehe   
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            danish = custom.Button.inline("โคโ ๐บ๐๐๐ ๐ธ๐๐๐ ๐ธ๐๐๐ ๐ฌ๐๐๐๐ โโฅ", data="open")
            await event.edit("`Main Menu Has Been Closed`", buttons=danish)
        else:
            reply_pop_up_alert = "Please get your own Userbot๐๐,for more info visit @DARK_COBRA_SUPPORT! ๐๐"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

  
    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            atul= "Please get your own Userbot๐๐,for more info visit @HunterXUserBot_SUPPORT! ๐๐"
            await event.answer(atul, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        global shivam_sh1vam
        shivam_sh1vam="{}".format(plugin_name)
        help_string = "Commands found in {}:\n".format(plugin_name)
        k = "๐?๐ฎ๐"
        u = 0
        for i in CMD_LIST[plugin_name]:
            u += 1
            help_string += str(k[u % 3]) + " " + i + "\n\n"
        if plugin_name in CMD_HELP:
            help_string += (
                f"**๐ค PLUGIN NAME ๐ค :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
            )
        else:
            help_string += "๐"

        reply_pop_up_alert = help_string
        reply_pop_up_alert += (
            "\n\n __Click on buttons below to load or unload them..report us if you find any bug__\n\n **ยฉDARKCOBRA USERBOT**".format(plugin_name)
        )
        try:
            if event.query.user_id == bot.uid :
                dc = [custom.Button.inline(" ๐ญ๐๐๐ ",data="back({})".format(shivam)),custom.Button.inline(" ๐ฎ๐๐๐๐ ", data="close"),custom.Button.inline(" ๐๐๐๐๐๐ ",data="unload({})".format(shivam_sh1vam))]
                await event.edit(reply_pop_up_alert, buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot, and don't use mine for more info visit @DARK_COBRA_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)#hehe
        except: 
            if event.query.user_id == bot.uid :
                sh1vam = [custom.Button.inline("โคโ ๐ฒ๐ ๐ญ๐๐๐ โโฅ",data="back({})".format(shivam)),custom.Button.inline("โคโ ๐ฎ๐๐๐๐ โโฅ", data="close")]
                halps = "Do .help {} to get the list of commands.".format(plugin_name)
                await event.edit(halps,buttons=sh1vam)
            else:
                reply_pop_up_alert = "Please get your own Userbot, and don't use mine for more info visit @DARK_COBRA_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"load\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              if event.query.user_id == bot.uid :
                    
#  ๐ฆโ๐ทโ๐ชโ     ๐งโ๐ธโ๐ฉโ๐ฐโ     ๐ฎโ๐ธโ๐ธโ๐ชโ   ๐ฐโ๐ฆโ๐ณโ๐ฌโ ๐ฒโ๐ฆโ๐นโ  ๐ฐโ๐ทโ   ๐ทโ๐ชโ  ๐ฒโ๐จโ
                    
                    try:
                        fcix = [custom.Button.inline("  ๐ญ๐๐๐ ",data="back({})".format(shivam)),custom.Button.inline(" ๐ฎ๐๐๐๐ ", data="close"),custom.Button.inline(" ๐๐๐๐๐๐ ",data="unload({})".format(shivam_sh1vam))]
                        load_module(event.data_match.group(1).decode("UTF-8"))# kyu sir kang krne m musil aa rhi h kya ... Bolo help kr du kya ๐๐๐
                        await event.edit( "`Your DarkCobra Has Successfully loaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e))+ "DarkCobra Has Successfully loaded" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  ๐ญ๐๐๐ ",data="back({})".format(shivam)),custom.Button.inline(" ๐ฎ๐๐๐๐ ", data="close"),custom.Button.inline(" ๐๐๐๐๐๐ ",data="unload({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot,for more info visit @DARK_COBRA_SUPPORT!"
                    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"unload\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              if event.query.user_id == bot.uid :
                    
                    
                    try:
                        fcix = [custom.Button.inline(" ๐ญ๐๐๐ ",data="back({})".format(shivam)),custom.Button.inline(" ๐ฎ๐๐๐๐ ", data="close"),custom.Button.inline(" ๐ท๐๐๐ ",data="load({})".format(shivam_sh1vam))]
                        remove_plugin(event.data_match.group(1).decode("UTF-8"))#kyu sir kang krne m muskil ho rhi h kya bologe toh help krdu ๐๐
                        await event.edit( "`Your DarkCobra Has Successfully unloaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e)) +"DarkCobra Has Successfully unloaded"+ str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  ๐ญ๐๐๐ ",data="back({})".format(shivam)),custom.Button.inline(" ๐ฎ๐๐๐๐ ", data="close"),custom.Button.inline(" ๐ท๐๐๐ ",data="load({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot,for more info visit @DARK_COBRA_SUPPORT!"
                    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)#hehehe
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
            
            if event.query.user_id == bot.uid :
                try:
                    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                    buttons = paginate_help(current_page_number-2, CMD_HELP, "helpme")
                    await event.edit("`>>> Here Is The Main Menu of\n\nยฉDARKCOBRA`", buttons=buttons)
                except:
                    buttons = paginate_help(0, CMD_HELP, "helpme")
                    await event.edit("`>>> Here Is The Main Menu Of\n\nยฉDARKCOBRA`", buttons=buttons)
            else:
                reply_pop_up_alert = "Please get your own Userbot,for more info visit @DARK_COBRA_SUPPORT!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    multi = Config.EMOJI_TO_DISPLAY_IN_HELP
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {}".format(random.choice(list(multi)), x),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    global shivam
    modulo_page = page_number % max_num_pages
    shivam=modulo_page
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("โขPREVIOUSโข", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("โขCLOSEโข", data="close"),
             custom.Button.inline("โขNEXTโข", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs

# chal nikal 
# gtfo
# SED aagye aap๐
