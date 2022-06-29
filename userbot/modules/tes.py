from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message)
from pyrogram import Client, filters 
from config import CMD_HANDLER as cmd 
import asyncio

@Client.on_message(filters.command(["help1"], cmd) & filters.me)
async def _create_keyboard_button(client, message):
        if isinstance(message, tuple):
            if 'http' in message[1]:
                return InlineKeyboardButton(text=tes[0], url=1[1])
            else:
                return InlineKeyboardButton(text=tes[0], callback_data=1[1])
        else:
            return InlineKeyboardButton(text=tes, callback_data=1)
