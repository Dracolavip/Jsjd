import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import enums
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from FallenMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from FallenMusic import app
from random import  choice, randint

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

from FallenMusic import app
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# ▒▒▒▗▉████████████▅▒▒▒▒▒▗██████████▄▒▒▒▄█████████▖▒▒▒▒▒▒▒▒▒▅████████▄▒▒▒▒▒▒▒▒▒▒
# ▒▒▒▝██████████████▒▒▒▒▒███████████▀▒▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒▒██▘▒▒▒▒▒▒▝██▒▒▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▄█▄▒▒███▒▒▒▒███▘▒▒▒██▒▒▒▝███▒▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒███▒▒███▒▒▒███▒▒▒▅████▄▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▀█▀▒▒███▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒█████████▖▒▒▒▒▒██████████▀▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒█████████▘▒▒▒▒▒███████▀▀▀▒▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒██▉▘▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒███▒▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒████▒▒▒███▒▒▒▒▒▒▒
# ▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒██▄▒▒▒██▒▒▒▄██▒▒▒▒▒▒▒▒
# ▒▒▒▗███████████████▅▒▒▒███████████▄▒▒▒███▒▒▒▒▒▒▒███▒▒▒▒▒▒██▖▒▒▒▒▒▒▗██▒▒▒▒▒▒▒▒▒
# ▒▒▒▀███████████████▀▒▒▒▝██████████▀▒▒▒███▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▀███████▀▒▒▒▒▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 
# (𝐂) 𝟐𝟎𝟐𝟒-𝟐𝟎𝟐𝟓 𝐛𝐲: @TopVeGa



@app.on_message(filters.command(["بحث"], ""), group=4458890044)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("يمكن البحث عبر فيجا")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("يتم البحث الان ...")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"⦿ العنوان : {results[i]['title']}\n"
            text += f"⦿ المدة : `{results[i]['duration']}`\n"
            text += f"⦿ المشاهدات : `{results[i]['views']}`\n"
            text += f"⦿ القناه : {results[i]['channel']}\n"
            text += f"⦿ الرابط : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "ＳＯＵＲＣＥ ＤＲＡＣＵＬＡ", url=f"https://t.me/D_A_003"),
                ],[
                    InlineKeyboardButton(
                        text="⸢✘⸥",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
