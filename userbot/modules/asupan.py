from random import choice
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from pyrogram.errors import RPCError

OJO = [-1001347414136, -1001578091827]


@Client.on_message(filters.command("asupan", cmd) & filters.me)
async def asupan(client: Client, message: Message):
    ppk = await message.edit("Sedang mencari video Asupan...")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_video(
        choice(
            [
                lol.video.file_id
                async for lol in Client.search_messages("@punyakenkan", filter="video")
            ]
        ),
        False,
        caption=f"Nih kak [{pop}](tg://user?id={ah}) Video Asupannya"
    )

    await ppk.delete()

@Client.on_message(filters.command("bokep", cmd) & filters.me)
async def bokep(client: Client, message: Message):
    ppk = await message.edit("Sedang mencari video bokep...")
    chat = message.chat.id
    if chat in OJO:
        await ppk.edit("**Maaf perintah ini dilarang di sini**")
        return
    elif chat not in OJO:
        await Client.send_video(chat, 
        choice(
            [
                lol.video.file_id
                async for lol in Client.search_messages("@fakyudurov", filter="video")
            ]
        ),
        False,
    )

    await ppk.delete()

@Client.on_message(filters.command("desah", cmd) & filters.me)
async def desah(client: Client, message: Message):
    ppk = await message.edit("`Sedang mencari voice desah...`")
    chat = message.chat.id
    if chat in OJO:
        await ppk.edit("**Maaf perintah ini dilarang di sini**")
        return
    elif chat not in OJO:
        await Client.send_voice(chat, 
        choice(
            [
                lol.voice.file_id
                async for lol in Client.search_messages("@punyakenkan", filter="voice_note")
            ]
        ),
        False,
    )

    await ppk.delete()


@Client.on_message(filters.command("logo", cmd) & filters.me)
async def logo(client: Client, message: Message):
    tod = await message.edit_text("`Memproses logo...`")
    chat = message.chat.id
    jembut = get_arg(message)
    pop = message.from_user.first_name
    ah = message.from_user.id
    bot = "oneupdirty_bot"
    if jembut:
        try:
            kk = await Client.send_message(bot, f"/logo {jembut}")
            await asyncio.sleep(10)
        except RPCError:
            await tod.edit("Silahkan buka blockir @oneupdirty_bot lalu coba lagi")
            return
        async for lol in Client.search_messages(bot, filter="photo", limit=1):
            if lol:
                await Client.send_photo(
                    chat,
                    photo=lol.photo.file_id,
                    caption=f"**Logo by:** [{pop}](tg://user?id={ah})",
                )
                await tod.delete()
                await kk.delete()
                await lol.delete()
            else:
                await Client.send_message(chat, "**Maaf ada yang salah**")
                await tod.delete()
    elif jembut:
        return await tod.edit("`Silahkan masukan nama logo`")
