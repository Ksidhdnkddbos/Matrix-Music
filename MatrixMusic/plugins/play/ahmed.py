import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait



@app.on_message(command(["المالك"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
            f = "administrators"
            async for member in client.get_chat_members(chat_id, filter=f):
               if member.status == "creator":
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"↯︙𝗈𝖶𝗇𝖤𝗋 ↬ ⦗ {m.first_name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ {m.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ `{m.id}` ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {m.bio} ⦘\n↯︙𝖦𝗋𝖮𝗎𝖯 ↬ ⦗ {message.chat.title} ⦘\n↯︙𝖦𝗋𝖮𝗎𝖯 𝖨𝖣 ↬ `{message.chat.id}`",reply_markup=key)
                 else:
                    return await message.reply("• " + member.user.mention)
