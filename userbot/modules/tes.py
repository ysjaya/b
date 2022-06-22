from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message)
from pyrogram import Client, filters 
from config import CMD_HANDLER as cmd 


@Client.on_message(filters.command(["help1"], cmd) & filters.me)
async def help1_message(client: Client, message):
  await message.reply_text(
      text="BayUserBot Modules",
      reply_markup=InlineKeyboardMarkup
      (
        [
          [
            InlineKeyboardButton("afk", url="t.me/euphoricfams"),
          ]
        ]
      )
    )

