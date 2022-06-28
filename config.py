

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🌹")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/5e82760d6ef347713720e.jpg")

ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.1.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "euphoricfams")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
MONGO_URI = getenv("MONGO_URI", "mongodb+srv://bayu:bayu@cluster0.tfdqy.mongodb.net/?retryWrites=true&w=majority")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX2R2RTVaM0NGZFBjVE1EVTUyQkdteE11NXJwRWcwNDQzV0pnZA==").decode(
        "utf-8"
    ),
)

GROUP = getenv("GROUP", "euphoricfams")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "https://telegra.ph/file/5e82760d6ef347713720e.jpg")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL3lzamF5YS9i").decode("utf-8"),
)

STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
