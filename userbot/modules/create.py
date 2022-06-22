

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from userbot.helpers.basic import edit_or_reply

from .help import add_command_help


@Client.on_message(filters.command("create", cmd) & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await edit_or_reply(
            message, f"**Ketik {cmd}help create bila membutuhkan bantuan**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    Man = await edit_or_reply(message, "`Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Berhasil Membuat Group Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Berhasil Membuat Channel Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "create",
    [
        [f"{cmd}create ch", "Untuk membuat channel telegram dengan userbot"],
        [f"{cmd}create gc", "Untuk membuat group telegram dengan userbot"],
    ],
)
