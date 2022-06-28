import os
import asyncio
from config import CMD_HANDLER as PREFIX
from pyrogram import filters
from pyrogram import Client as kontol
from .help import add_command_help
import userbot.database.pmpermitdb as Primedb
from userbot.helpers.PyroHelpers import denied_users, get_arg



FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}
PM_LOGO = os.environ.get("ALIVE_LOGO")

@kontol.on_message(filters.command("pmguard", PREFIX) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Saya hanya mengerti on atau off**")
        return
    if arg == "off":
        await Primedb.set_pm(False)
        await message.edit("**PM Guard Dinonaktifkan**")
    if arg == "on":
        await Primedb.set_pm(True)
        await message.edit("**PM Guard Diaktifkan**")


@kontol.on_message(filters.command("setlimit", PREFIX) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Tetapkan batas untuk apa?**")
        return
    await Primedb.set_limit(int(arg))
    await message.edit(f"**Batas disetel ke {arg}**")
    
@kontol.on_message(filters.command("setpmmsg", PREFIX) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Pesan apa yang akan disetel**")
        return
    if arg == "default":
        await Primedb.set_permit_message(Primedb.PMPERMIT_MESSAGE)
        await message.edit("**Pesan Anti-PM disetel ke default**.")
        return
    await Primedb.set_permit_message(f"{arg}")
    await message.edit("**Set pesan Anti-PM khusus**")


@kontol.on_message(filters.command("setblockmsg", PREFIX) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Pesan apa yang akan disetel**")
        return
    if arg == "default":
        await Primedb.set_block_message(Primedb.BLOCKED)
        await message.edit("**Blokir pesan disetel ke default**.")
        return
    await Primedb.set_block_message(f"{arg}")
    await message.edit("**Set pesan blokir khusus**")


@kontol.on_message(filters.command(["allow", "a"], PREFIX) & filters.me & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await Primedb.get_pm_settings()
    await Primedb.allow_user(chat_id)
    await message.edit(f"**Saya telah mengizinkan [Anda](tg://user?id={chat_id}) untuk PM saya.**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@kontol.on_message(filters.command(["deny", "d"], PREFIX) & filters.me & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await Primedb.deny_user(chat_id)
    await message.edit(f"**Saya telah menolak [Anda](tg://user?id={chat_id}) untuk PM saya.**")


@kontol.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await Primedb.get_pm_settings()
    user = message.from_user.id
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]
    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return
        async for message in client.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await message.delete()
        if not PM_LOGO:
            await message.reply(pm_message, disable_web_page_preview=True)
        else:
            ahh = client.send_video if PM_LOGO.endswith(".mp4") else client.send_photo
            await asyncio.gather(
                    ahh(
                        message.chat.id,
                        PM_LOGO,
                        caption=pm_message
                    ),
                )
            return
    await message.reply(block_message, disable_web_page_preview=True)
    await client.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})


add_command_help(
    "pmpermit",
    [
        [
            f"{cmd}ok atau {cmd}a",
            "Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            f"{cmd}tolak atau {cmd}t",
            "Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            f"{cmd}pmlimit <angka>",
            "Untuk mengcustom pesan limit auto block pesan",
        ],
        [
            f"{cmd}setpmpermit <balas ke pesan>",
            "Untuk mengcustom pesan PMPERMIT untuk orang yang pesannya belum diterima.",
        ],
        [
            f"{cmd}getpmpermit",
            "Untuk melihat pesan PMPERMIT.",
        ],
        [
            f"{cmd}resetpmpermit",
            "Untuk Mereset Pesan PMPERMIT menjadi DEFAULT",
        ],
        [
            f"{cmd}setvar PM_AUTO_BAN True",
            "Perintah untuk mengaktifkan PMPERMIT",
        ],
        [
            f"{cmd}setvar PM_AUTO_BAN False",
            "Perintah untuk mennonaktifkan PMPERMIT",
        ],
    ],
)
