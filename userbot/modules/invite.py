

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from userbot.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.me & filters.command("invite", cmd))
async def inviteee(client: Client, message: Message):
    mg = await edit_or_reply(message, "`Adding Users!`")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")


@Client.on_message(filters.command(["inviteall"], cmd) & filters.me)
async def inviteall(client, message):
    ken = await message.edit_text(f"⚡ Berikan saya username group. contoh: {cmd}inviteall @euphoricfams")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    kontol = 0
    gagal = 0
    await ken.edit_text(f"Menambahkan members dari {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user = member.user
        zxb = ["online", "offline", "recently", "within_week"]
        if user.status in zxb:
            try:
                await client.add_chat_members(tgchat.id, user.id, forward_limit=60)
                kontol = kontol + 1
                await asyncio.sleep(2)
            except FloodWait as e:
                mg = await client.send_message(LOG_CHAT, f"error-   {e}")
                gagal = gagal + 1
                await asyncio.sleep(0.3)
                await mg.delete()
                
    return await client.send_message(tgchat.id, f"**Invite All** \n\n**Berhasil:** `{kontol}`\n**Gagal:** `{gagal}`"
    )

@Client.on_message(filters.command("invitelink", cmd) & filters.me)
async def invite_link(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    if message.chat.type in ["group", "supergroup"]:
        message.chat.title
        try:
            link = await client.export_chat_invite_link(message.chat.id)
            await Man.edit(f"Link Invite: {link}")
        except Exception:
            await Man.edit("Denied permission")


add_command_help(
    "invite",
    [
        [
            f"{cmd}invitelink",
            "Untuk Mendapatkan Link invite ke grup Obrolan Anda. [Need Admin]",
        ],
        [f"{cmd}invite @username", "Untuk Mengundang Anggota ke grup Anda."],
        [
            f"{cmd}inviteall @usernamegc",
            "Untuk Mengundang Anggota dari obrolan grup lain ke obrolan grup Anda.",
        ],
    ],
)
