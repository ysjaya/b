

import html

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from userbot.helpers.basic import edit_or_reply
from userbot.helpers.parser import mention_html, mention_markdown
from userbot.modules.help import *
from userbot.helpers.PyroHelpers import *

@Client.on_message(filters.me & filters.command(["admins", "adminlist"], cmd))
async def adminlist(client: Client, message: Message):
    replyid = None
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.message_id
    alladmins = client.iter_chat_members(chat, filter="administrators")
    creator = []
    admin = []
    badmin = []
    async for a in alladmins:
        try:
            nama = a.user.first_name + " " + a.user.last_name
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.status == "administrator":
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, nama))
            else:
                admin.append(mention_markdown(a.user.id, nama))
        elif a.status == "creator":
            creator.append(mention_markdown(a.user.id, nama))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = "**Admins in {}**\n".format(grup.title)
    teks += "╒═══「 Creator 」\n"
    for x in creator:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} Human Administrator 」\n".format(len(admin))
    for x in admin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} Bot Administrator 」\n".format(len(badmin))
    for x in badmin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╘══「 Total {} Admins 」".format(totaladmins)
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


@Client.on_message(filters.command(["kickdel", "zombies"], cmd) & filters.me)
async def kickdel_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "<b>Kicking deleted accounts...</b>")
    # noinspection PyTypeChecker
    values = [
        await message.chat.ban_member(user.user.id, int(time()) + 31)
        for member in await message.chat.get_members()
        if member.user.is_deleted
    ]
    await Man.edit(f"<b>Successfully kicked {len(values)} deleted account(s)</b>")


@Client.on_message(
    filters.me & filters.command(["reportadmin", "reportadmins", "report"], cmd)
)
async def report_admin(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    alladmins = client.iter_chat_members(message.chat.id, filter="administrators")
    admin = []
    async for a in alladmins:
        if a.status == "administrator" or a.status == "creator":
            if not a.user.is_bot:
                admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        if text:
            teks = "{}".format(text)
        else:
            teks = "{} reported to admins.".format(
                mention_html(
                    message.reply_to_message.from_user.id,
                    message.reply_to_message.from_user.first_name,
                )
            )
    else:
        if text:
            teks = "{}".format(html.escape(text))
        else:
            teks = "Calling admins in {}.".format(grup.title)
    teks += "".join(admin)
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            teks,
            reply_to_message_id=message.reply_to_message.message_id,
            parse_mode="html",
        )
    else:
        await client.send_message(message.chat.id, teks, parse_mode="html")


@Client.on_message(filters.me & filters.command(["everyone", "tagall"], cmd))
async def tag_all_users(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    tai = message.reply_to_message
    ppk = get_arg(message)
    if not tai and not ppk:
        return await message.edit("__Tolong berikan saya pesan atau balas ke pesan!__")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    async for usr in app.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if ppk:
                txt = f"{ppk}\n{usrtxt}"
                await app.send_message(chat_id, txt)
            elif tai:
                await tai.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ''
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@Client.on_message(filters.me & filters.command(["botlist", "bots"], cmd))
async def get_list_bots(client: Client, message: Message):
    replyid = None
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.message_id
    getbots = client.iter_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            nama = a.user.first_name + " " + a.user.last_name
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, nama))
    teks = "**All bots in group {}**\n".format(grup.title)
    teks += "╒═══「 Bots 」\n"
    for x in bots:
        teks += "│ • {}\n".format(x)
    teks += "╘══「 Total {} Bots 」".format(len(bots))
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


add_command_help(
    "tag",
    [
        [f"{cmd}admins", "Get chats Admins list."],
        [f"{cmd}kickdel", "To Kick deleted Accounts."],
        [
            f"{cmd}everyone `or` {cmd}tagall",
            "to mention Everyone ",
        ],
        [
            f"{cmd}botlist",
            "To get Chats Bots list",
        ],
    ],
)
