
import asyncio
import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from config import *
from userbot import StartTime
from userbot.helpers.basic import edit_or_reply
from userbot.helpers.constants import WWW
from userbot.helpers.constants import *
from userbot.helpers.expand import expand_url
from userbot.helpers.PyroHelpers import SpeedConvert
from userbot.helpers.shorten import shorten_url
from userbot.utils.tools import get_readable_time

from .help import add_command_help


@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(filters.command("ping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
   
    xx = await edit_or_reply(message, "🎉")
    
    await asyncio.sleep(2)
    yy = await edit_or_reply(message, "BLACKPINK")
    await asyncio.sleep(2)
    await yy.edit("AYE!! AYE!!")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    output = (
        
        f"❏ **DUAR MEMEW!!💦**\n"
        f"├• **Pinger** - `%sms`\n"
        f"├• **Uptime -** `{uptime}` \n"
        f"└• **Owner :** {client.me.mention}" % (duration)
    )
  
    await client.send_photo(message.chat.id, photo=ALIVE_LOGO, caption=output)
    await xx.delete()


@Client.on_message(filters.command("expand", cmd) & filters.me)
async def expand(client: Client, message: Message):
    if message.reply_to_message:
        url = message.reply_to_message.text or message.reply_to_message.caption
    elif len(message.command) > 1:
        url = message.command[1]
    else:
        url = None

    if url:
        expanded = await expand_url(url)
        if expanded:
            await message.edit(
                f"<b>Shortened URL</b>: {url}\n<b>Expanded URL</b>: {expanded}",
                disable_web_page_preview=True,
            )
        else:
            await message.edit("No bro that's not what I do")
    else:
        await message.edit("Nothing to expand")


@Client.on_message(filters.command("shorten", cmd) & filters.me)
async def shorten(client: Client, message: Message):
    keyword = None

    if message.reply_to_message:
        url = message.reply_to_message.text or message.reply_to_message.caption
        if len(message.command) > 1:
            keyword = message.command[1]
    elif len(message.command) > 2:
        url = message.command[1]
        keyword = message.command[2]
    elif len(message.command) > 1:
        url = message.command[1]
    else:
        url = None

    if url:
        shortened = await shorten_url(url, keyword)
        if shortened == "API ERROR":
            txt = "API URL or API KEY not found! Add YOURLS details to config"
        elif shortened == "INVALID URL":
            txt = f"The provided URL: `{url}` is invalid"
        elif shortened == "KEYWORD/URL Exists":
            txt = "The URL or KEYWORD already exists!"
        else:
            txt = f"<b>Original URL</b>: {url}\n<b>Shortened URL</b>: {shortened}"
            await message.edit(txt, disable_web_page_preview=True)
            return
    else:
        txt = "Please provide a URL to shorten"

    await message.edit(txt)
    await asyncio.sleep(3)
    await message.delete()


add_command_help(
    "www",
    [
        [f"{cmd}ping", "Calculates ping time between you and Telegram."],
        [f"{cmd}dc", "Get's your Telegram DC."],
        [
            f"{cmd}speedtest `or` {cmd}speed",
            "Runs a speedtest on the server this userbot is hosted.. Flex on them haters. With an in "
            "Telegram Speedtest of your server..",
        ],
        [
            f"{cmd}expand",
            "Expands a shortened url. Works for replied to message, photo caption or .expand url",
        ],
        [
            f"{cmd}shorten",
            "Shortens a url. Works for replied to message, photo caption or .shorten url keyword",
        ],
    ],
)
