

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from userbot.helpers.basic import edit_or_reply

from .help import *





@Client.on_message(filters.me & filters.command("asupan", cmd))
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")



@Client.on_message(filters.me & filters.command("bokep", cmd))
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            bokep
            async for bokep in event.client.iter_messages(
                "@fakyudurov", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")




@Client.on_message(filters.me & filters.command("desah", cmd))
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            desahan
            async for desahan in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice_Note
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahanya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahann.**")

