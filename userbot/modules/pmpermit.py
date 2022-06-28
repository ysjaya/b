from pyrogram import Client, filters
from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError
import asyncio
import time
from config import CMD_HANDLER as cmd
from config import PM_AUTO_BAN
from userbot import TEMP_SETTINGS

from .help import *


DEF_UNAPPROVED_MSG = f" 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 🔱 \n\n"
DEF_UNAPPROVED_MSG += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
DEF_UNAPPROVED_MSG += f"► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
DEF_UNAPPROVED_MSG += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
DEF_UNAPPROVED_MSG += f"► Rᴇᴘᴏ : [Deploy On Bot](https://telegram.dog/XTZ_HerokuBot?start=eXNqYXlhL2JheXVzZXJib3QgbWFpbg) \n"
DEF_UNAPPROVED_MSG += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/ygabutkan) \n"
DEF_UNAPPROVED_MSG += f"► Mutualan : [Jᴏɪɴ.](https://t.me/euphoricfams) \n"
DEF_UNAPPROVED_MSG += f"⍟ 𝙹𝙰𝙽𝙶𝙰𝙽 𝚂𝙿𝙰𝙼 𝙲𝙷𝙰𝚃 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙺𝙴𝙽𝚃𝙾𝙳⍟\n⍟ 𝙶𝚄𝙰 𝙰𝙺𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𝙱𝙻𝙾𝙺𝙸𝚁 𝙺𝙰𝙻𝙾 𝙻𝚄 𝚂𝙿𝙰𝙼⍟\n⍟ 𝙹𝙰𝙳𝙸 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙰𝙼𝙿𝙰𝙸 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙽𝙴𝚁𝙸𝙼𝙰 𝙿𝙴𝚂𝙰𝙽 𝙻𝚄⍟\n"
DEF_UNAPPROVED_MSG += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"




@Client.on_message(
    ~filters.me & filters.private & ~filters.bot & filters.incoming, group=69
)
async def incomingpm(client: Client, message: Message):
    if not PM_AUTO_BAN:
        message.continue_propagation()
    else:
        if message.chat.id != 777000:
            try:
                from userbot.helpers.SQL.globals import gvarstatus
                from userbot.helpers.SQL.pm_permit_sql import is_approved
            except BaseException:
                pass

            PM_LIMIT = gvarstatus("PM_LIMIT") or 5
            getmsg = gvarstatus("unapproved_msg")
            if getmsg is not None:
                UNAPPROVED_MSG = getmsg
            else:
                UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

            apprv = is_approved(message.chat.id)
            if not apprv and message.text != UNAPPROVED_MSG:
                if message.chat.id in TEMP_SETTINGS["PM_LAST_MSG"]:
                    prevmsg = TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                    if message.text != prevmsg:
                        async for message in client.search_messages(
                            message.chat.id,
                            from_user="me",
                            limit=10,
                            query=UNAPPROVED_MSG,
                        ):
                           await message.delete()
                        if TEMP_SETTINGS["PM_COUNT"][message.chat.id] < (
                            int(PM_LIMIT) - 1
                        ):
                            ret = await message.reply_text(UNAPPROVED_MSG)
                            TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
                else:
                    ret = await client.send_photo(message.chat.id, photo=ALIVE_LOGO, caption=UNAPPROVED_MSG)
                    await asyncio.sleep(10)
                    await ret.delete()
                    if ret.text:
                        TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text

                if message.chat.id not in TEMP_SETTINGS["PM_COUNT"]:
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] = 1
                else:
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] = (
                        TEMP_SETTINGS["PM_COUNT"][message.chat.id] + 1
                    )
                            
                if TEMP_SETTINGS["PM_COUNT"][message.chat.id] > (int(PM_LIMIT) - 1):
                    await message.reply("**DI BILANGIN JANGAN SPAM KOK NGEYEL**")

                    try:
                        del TEMP_SETTINGS["PM_COUNT"][message.chat.id]
                        del TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                    except BaseException:
                        pass

                    await client.block_user(message.chat.id)
    
    
    message.continue_propagation()
    


@Client.on_message(
    filters.command(["ok", "a", "approve"], cmd) & filters.me & filters.private
)
async def approvepm(client: Client, message: Message):
    try:
        from userbot.helpers.SQL.pm_permit_sql import approve
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("Anda tidak dapat menyetujui diri sendiri.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == "private":
            await message.edit(
                "Saat ini Anda tidak sedang dalam PM dan Anda belum membalas pesan seseorang."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    try:
        approve(uid)
        xx = await message.edit(f"**Menerima Pesan Dari** [{name0}](tg://user?id={uid})!")
    except IntegrityError:
        xx = await message.edit(
            f"[{name0}](tg://user?id={uid}) mungkin sudah disetujui untuk PM."
        )
        return
        await asyncio.sleep(3)
        await xx.delete()
        
    


@Client.on_message(
    filters.command(["tolak", "t", "disapprove"], cmd) & filters.me & filters.private
)
async def disapprovepm(client: Client, message: Message):
    try:
        from userbot.helpers.SQL.pm_permit_sql import dissprove
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("Anda tidak bisa menolak dirimu sendiri.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == "private":
            await message.edit(
                "Saat ini Anda tidak sedang dalam PM dan Anda belum membalas pesan seseorang."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    dissprove(uid)

    await message.edit(
        f"**Pesan** [{name0}](tg://user?id={uid}) **Telah Ditolak, Mohon Jangan Melakukan Spam Chat!**"
    )


@Client.on_message(filters.command("pmlimit", cmd) & filters.me)
async def setpm_limit(client: Client, cust_msg: Message):
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            f"**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `{cmd}setvar PM_AUTO_BAN True`"
        )
    try:
        from userbot.helpers.SQL.globals import addgvar
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    input_str = (
        cust_msg.text.split(None, 1)[1]
        if len(
            cust_msg.command,
        )
        != 1
        else None
    )
    if not input_str:
        return await cust_msg.edit("**Harap masukan angka untuk PM_LIMIT.**")
    Man = await cust_msg.edit("`Processing...`")
    if input_str and not input_str.isnumeric():
        return await Man.edit("**Harap masukan angka untuk PM_LIMIT.**")
    addgvar("PM_LIMIT", input_str)
    await Man.edit(f"**Set PM limit to** `{input_str}`")


@Client.on_message(filters.command("setpmpermit", cmd) & filters.me)
async def setpmpermit(client: Client, cust_msg: Message):
    """Set your own Unapproved message"""
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            "**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `.setvar PM_AUTO_BAN True`"
        )
    try:
        import userbot.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    Man = await cust_msg.edit("`Processing...`")
    custom_message = sql.gvarstatus("unapproved_msg")
    message = cust_msg.reply_to_message
    if custom_message is not None:
        sql.delgvar("unapproved_msg")
    if not message:
        return await Man.edit("**Mohon Reply Ke Pesan**")
    msg = message.text
    sql.addgvar("unapproved_msg", msg)
    await Man.edit("**Pesan Berhasil Disimpan Ke Room Chat**")


@Client.on_message(filters.command("getpmpermit", cmd) & filters.me)
async def get_pmermit(client: Client, cust_msg: Message):
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            "**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `.setvar PM_AUTO_BAN True`"
        )
    try:
        import userbot.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    Man = await cust_msg.edit("`Processing...`")
    custom_message = sql.gvarstatus("unapproved_msg")
    if custom_message is not None:
        await Man.edit("**Pesan PMPERMIT Yang Sekarang:**" f"\n\n{custom_message}")
    else:
        await Man.edit(
            "**Anda Belum Menyetel Pesan Costum PMPERMIT,**\n"
            f"**Masih Menggunakan Pesan PM Default:**\n\n{DEF_UNAPPROVED_MSG}"
        )


@Client.on_message(filters.command("resetpmpermit", cmd) & filters.me)
async def reset_pmpermit(client: Client, cust_msg: Message):
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            f"**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `{cmd}setvar PM_AUTO_BAN True`"
        )
    try:
        import userbot.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    Man = await cust_msg.edit("`Processing...`")
    custom_message = sql.gvarstatus("unapproved_msg")

    if custom_message is None:
        await Man.edit("**Pesan PMPERMIT Anda Sudah Default**")
    else:
        sql.delgvar("unapproved_msg")
        await Man.edit("**Berhasil Mengubah Pesan Custom PMPERMIT menjadi Default**")


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
