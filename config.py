import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "xAbhish3k")
ALIVE_NAME = getenv("ALIVE_NAME", "xAbhish3k")
BOT_USERNAME = getenv("BOT_USERNAME", "camillamusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "warbotzsupport")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "warbotz")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheWarBotZ")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5e2da7a50d090e37dd665.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/xAbhish3k/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/68e64e7a21d21da897971.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/03724c51b72ddd985616c.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/388491ec29207d78454f4.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/5e2da7a50d090e37dd665.png")
