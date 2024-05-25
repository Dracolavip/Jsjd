from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID", "6586941458"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1c198ce7e477a1424fbad.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1c198ce7e477a1424fbad.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/vv_jj_7")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/D_A_003")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6586941458").split()))


FAILED = "https://telegra.ph/file/1c198ce7e477a1424fbad.jpg"
