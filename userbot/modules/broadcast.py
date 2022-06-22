

import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from requests import get

from config import CMD_HANDLER as cmd
from userbot.helpers.adminHelpers import DEVS
from userbot.helpers.basic import edit_or_reply

from .help import add_command_help

_GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/mrismanaziz/Reforestation/master/blacklistgcast.json"
    ) 
    
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001763422160]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@Client.on_message(filters.command("gcast", cmd) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await edit_or_reply(message, "**Berikan Sebuah Pesan atau Reply**")
    Man = await edit_or_reply(message, "`Started global broadcast...`")
    done = 0
    error = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ("group", "supergroup"):
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await client.send_message(chat, text)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    await client.send_message(chat, text)
                except Exception:
                    error += 1
    await Man.edit_text(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{error}` **Grup**"
    )


@Client.on_message(filters.command("gucast", cmd) & filters.me)
async def gucast_cmd(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await edit_or_reply(message, "**Berikan Sebuah Pesan atau Reply**")
    Man = await edit_or_reply(message, "`Started global broadcast to users...`")
    done = 0
    error = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type == "private" and not dialog.chat.is_verified:
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    await client.send_message(chat, text)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    await client.send_message(chat, text)
                except Exception:
                    error += 1
    await Man.edit_text(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{error}` **chat**"
    )


add_command_help(
    "broadcast",
    [
        [
            f"{cmd}gcast <text/reply>",
            "Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk.",
        ],
        [
            f"{cmd}gucast <text/reply>",
            "Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk.",
        ],
    ],
)
