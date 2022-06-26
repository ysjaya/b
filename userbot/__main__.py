

import importlib

from pyrogram import idle

from config import *
from userbot import BOTLOG_CHATID, LOGGER, LOOP, bots
from userbot.helpers.misc import git, heroku
from userbot.modules import ALL_MODULES

MSG_ON = """
🌹 **BayUserbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━🌹
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"userbot.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ygabutkan")
            await bot.join_chat("ygabutkan")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()


if __name__ == "__main__":
    LOGGER("userbot").info("Starting BayUserBot")
    LOGGER("userbot").info(f"Total Clients = {len(bots)} Users")
    git()
    heroku()
    LOGGER("userbot").info(f"BayUserBot v{BOT_VER} [🌹 BERHASIL DIAKTIFKAN! 🌹]")
    LOOP.run_until_complete(main())
