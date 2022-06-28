# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved.

from . import cli
from config import *

collection = cli["Prime"]["pmpermit"]

PMPERMIT_MESSAGE = (
    " 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 🔱 \n\n"
    "◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
    "► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
    "► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
    "► Rᴇᴘᴏ : [Deploy On Bot](https://telegram.dog/XTZ_HerokuBot?start=eXNqYXlhL2JheXVzZXJib3QgbWFpbg) \n"
    "► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/ygabutkan) \n"
    "► Gc Mutualan : [Jᴏɪɴ.](https://t.me/euphoricfams) \n"
    "⍟ 𝙹𝙰𝙽𝙶𝙰𝙽 𝚂𝙿𝙰𝙼 𝙲𝙷𝙰𝚃 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙺𝙴𝙽𝚃𝙾𝙳⍟\n⍟ 𝙶𝚄𝙰 𝙰𝙺𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𝙱𝙻𝙾𝙺𝙸𝚁 𝙺𝙰𝙻𝙾 𝙻𝚄 𝚂𝙿𝙰𝙼⍟\n⍟ 𝙹𝙰𝙳𝙸 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙰𝙼𝙿𝙰𝙸 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙽𝙴𝚁𝙸𝙼𝙰 𝙿𝙴𝚂𝙰𝙽 𝙻𝚄⍟\n"
    "◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"

)

BLOCKED = (
    "**Anda Telah Di Blokir Karna Melakukan Spam Pesan\nKe Room Chat Prime Userbot ツ**"
)

LIMIT = 5
LOGO_PM = ALIVE_LOGO

async def set_pm(value: bool):
    doc = {"_id": 1, "pmpermit": value}
    doc2 = {"_id": "Approved", "users": []}
    r = await collection.find_one({"_id": 1})
    r2 = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": 1}, {"$set": {"pmpermit": value}})
    else:
        await collection.insert_one(doc)
    if not r2:
        await collection.insert_one(doc2)


async def set_permit_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"pmpermit_message": text}})

async def set_logo_pm(text):
    await collection.update_one({"_id": 1}, {"$set": {"logo_pm": text}})
    
async def set_block_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"block_message": text}})


async def set_limit(limit):
    await collection.update_one({"_id": 1}, {"$set": {"limit": limit}})


async def get_pm_settings():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    pmpermit = result["pmpermit"]
    pm_message = result.get("pmpermit_message", PMPERMIT_MESSAGE)
    block_message = result.get("block_message", BLOCKED)
    limit = result.get("limit", LIMIT)
    logo_pm = result.get("logo_pm", LOGO_PM)
    return pmpermit, pm_message, limit, block_message, logo_pm


async def allow_user(chat):
    doc = {"_id": "Approved", "users": [chat]}
    r = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": "Approved"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_approved_users():
    results = await collection.find_one({"_id": "Approved"})
    if results:
        return results["users"]
    else:
        return []


async def deny_user(chat):
    await collection.update_one({"_id": "Approved"}, {"$pull": {"users": chat}})


async def pm_guard():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    if not result["pmpermit"]:
        return False
    else:
        return True
