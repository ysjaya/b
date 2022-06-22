

import asyncio
import os

from pyrogram import Client, filters, raw
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from userbot import *
from userbot.helpers.basic import edit_or_reply
from userbot.utils import s_paste

from .help import *


@Client.on_message(filters.command("limit", cmd) & filters.me)
async def spamban(client: Client, m: Message):
    await client.unblock_user("SpamBot")
    response = await client.send(
        raw.functions.messages.StartBot(
            bot=await client.resolve_peer("SpamBot"),
            peer=await client.resolve_peer("SpamBot"),
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    wait_msg = await edit_or_reply(m, "`Processing...`")
    await asyncio.sleep(1)
    spambot_msg = response.updates[1].message.id + 1
    status = await client.get_messages(chat_id="SpamBot", message_ids=spambot_msg)
    await wait_msg.edit_text(f"~ {status.text}")


@Client.on_message(filters.command("webshot" "ss", cmd) & filters.me)
async def webshot(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    try:
        user_link = message.command[1]
        try:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Screenshot of the page ⟶** {user_link}",
            )
        except Exception as dontload:
            await message.edit(f"Error! {dontload}\nTrying again create screenshot...")
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Screenshot of the page ⟶** {user_link}",
            )
        await Man.delete()
    except Exception as error:
        await Man.delete()
        await client.send_message(
            message.chat.id, f"**Something went wrong\nLog:{error}...**"
        )


@Client.on_message(filters.command("type", cmd) & filters.me)
async def types(client: Client, message: Message):
    orig_text = message.text.split(prefix + "type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while tbp != orig_text:
        await message.edit(str(tbp + typing_symbol))
        await asyncio.sleep(0.10)
        tbp = tbp + text[0]
        text = text[1:]
        await message.edit(str(tbp))
        await asyncio.sleep(0.10)


@Client.on_message(filters.command(["directmessage", "dm"], cmd) & filters.me)
async def deem(client: Client, message: Message):
    Man = await edit_or_reply(message, "⚡ Usage:\n .dm @username Umm")
    quantity = 1
    inp = message.text.split(None, 2)[1]
    user = await client.get_chat(inp)
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await Man.edit("Message Sended Successfully ✅")
            await client.send_message(
                user.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(user.id, spam_text)
        await Man.edit("Message Sended Successfully ✅")
        await asyncio.sleep(0.15)


@Client.on_message(filters.command("duck", cmd) & filters.me)
async def duckgo(client: Client, message: Message):
    input_str = " ".join(message.command[1:])
    Man = await edit_or_reply(message, "`Processing...`")
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ", "+"))
    if sample_url:
        link = sample_url.rstrip()
        await Man.edit_text(
            "Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(input_str, link)
        )
    else:
        await Man.edit_text("something is wrong. please try again later.")


@Client.on_message(filters.command("open", cmd) & filters.me)
async def open_file(client: Client, m: Message):
    xd = await edit_or_reply(m, "`Reading File!`")
    f = await client.download_media(m.reply_to_message)
    if f:
        _error = open(f, "r")
        _error_ = _error.read()
        _error.close()
        if len(_error_) >= 4096:
            await xd.edit("`Pasting to Spacebin!`")
            ext = "py"
            x = await s_paste(_error_, ext)
            s_link = x["url"]
            s_raw = x["raw"]
            pasted = f"**Pasted to Spacebin**\n**Link:** [Spacebin]({s_link})\n**Raw Link:** [Raw]({s_raw})"
            return await xd.edit(pasted, disable_web_page_preview=True)
        else:
            await xd.edit(f"**Output:**\n```{_error_}```")
    else:
        await edit_or_reply(m, "Reply to a File to open it!")
        os.remove(f)


add_command_help(
    "misc",
    [
        [f"{cmd}limit", "Check Limit telegram from @SpamBot."],
        [
            f"{cmd}dm <username> <text>",
            "Untuk mengirim chat dengan menggunakan userbot.",
        ],
        [f"{cmd}duck", "Untuk mendapatkan Link dari DuckDuckGo."],
        [
            f"{cmd}open",
            "Untuk melihat isi File menjadi text yang dikirim menjadi pesan telegram.",
        ],
    ],
)


add_command_help(
    "webshot",
    [
        [f"{cmd}webshot", "screenshot the given webpage ."],
    ],
)
