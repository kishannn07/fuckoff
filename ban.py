#  Copyright (c) 2022 @TheRiZoeL - RiZoeL
# Telegram Ban All Bot 
# Creator - RiZoeL

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var


logging.basicConfig(level=logging.INFO)

print("Starting.....")

Riz = TelegramClient('Riz', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@Riz.on(events.NewMessage(pattern="^!thanos"))  
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "!BADNAM"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**I'm On** \n\n _⚡𝙎𝙪𝙧𝙥𝙞𝙨𝙚 𝙎𝙪𝙧𝙥𝙧𝙞𝙨𝙚 𝙢𝙤𝙩𝙝𝙚𝙧 𝙁𝙪𝙘𝙠𝙚𝙧𝙨_ !! `{ms}` ms")


@Riz.on(events.NewMessage(pattern="^!fuckoff"))
async def testing(event):
  if event.sender_id in SUDO_USERS:
   if not event.is_group:
        Reply = f"Noob !! Use This Cmd in Group."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       RiZoeL = await event.get_chat()
       RiZoeLop = await event.client.get_me()
       admin = RiZoeL.admin_rights
       creator = RiZoeL.creator
       if not admin and not creator:
           await event.reply("𝙉𝙤𝙤𝙗 !! 𝙋𝙝𝙚𝙡𝙚 𝘼𝙙𝙢𝙞𝙣 𝘽𝙖𝙣𝙖 !!")
           return
       await event.reply("𝙏𝙃𝙀 !! 𝙆𝙄𝙉𝙂 𝙄𝙎 𝘽𝘼𝘾𝙆 👹")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == RiZoeLop.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@Riz.on(events.NewMessage(pattern="^!leave"))
async def _(e):
    if e.sender_id in SUDO_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            bc = int(bc)
            text = "Badnam....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("! 𝙅𝙝𝙪𝙠𝙚𝙜𝙖 𝙉𝙝𝙞𝙞 𝙅𝙝𝙪𝙠𝙖 𝙆𝙖𝙧 𝙡𝙚𝙂𝙖")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Badnam....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("!!𝙅𝙃𝙐𝙆𝘼 𝙆𝘼𝙍 𝙇𝙀 𝙇𝙄𝙔𝘼 𝘼𝘽 𝙈𝘼𝙄 𝘾𝙃𝘼𝙇𝘼!!")
            except Exception as e:
                await event.edit(str(e))   
          


@Riz.on(events.NewMessage(pattern="^!Pushpa"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = " 🔥𝙛𝙞𝙧𝙚 𝙝𝙖𝙞 𝘼𝙥𝙪𝙣 ...☠!!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Riz.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("🔥__BADNAM__")

Riz.run_until_disconnected()
