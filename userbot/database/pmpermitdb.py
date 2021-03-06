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
    " ππ¬ππ«ππ¨π­ ππ«π’π―ππ­π ππ«π¨π­πππ­π’π¨π§ π± \n\n"
    "β ββββββ β ββββββ β \n"
    "βΊ α΄ α΄ΚsΙͺα΄Ι΄ : `Beta.0.1` \n"
    "βΊ α΄ΚΚα΄ α΄ α΄ΚsΙͺα΄Ι΄ : `1.4.15` \n"
    "βΊ Rα΄α΄α΄ : [Deploy On Bot](https://telegram.dog/XTZ_HerokuBot?start=eXNqYXlhL2JheXVzZXJib3QgbWFpbg) \n"
    "βΊ Sα΄α΄α΄α΄Κα΄ : [Jα΄ΙͺΙ΄.](https://t.me/ygabutkan) \n"
    "βΊ Gc Mutualan : [Jα΄ΙͺΙ΄.](https://t.me/euphoricfams) \n"
    "β πΉπ°π½πΆπ°π½ ππΏπ°πΌ π²π·π°π πΌπ°πΉπΈπΊπ°π½ πΆππ° πΊπ΄π½ππΎπ³β\nβ πΆππ° π°πΊπ°π½ πΎππΎπΌπ°ππΈπ π±π»πΎπΊπΈπ πΊπ°π»πΎ π»π ππΏπ°πΌβ\nβ πΉπ°π³πΈ πππ½πΆπΆπ ππ°πΌπΏπ°πΈ πΌπ°πΉπΈπΊπ°π½ πΆππ° π½π΄ππΈπΌπ° πΏπ΄ππ°π½ π»πβ\n"
    "β ββββββ β ββββββ β \n\n"

)

BLOCKED = (
    "**Anda Telah Di Blokir Karna Melakukan Spam Pesan\nKe Room Chat Prime Userbot γ**"
)

LIMIT = 5

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
    return pmpermit, pm_message, limit, block_message


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
