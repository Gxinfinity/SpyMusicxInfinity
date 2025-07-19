import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "26950458"))

API_HASH = getenv("API_HASH", "d818b8d530e4a9b209509815ab1b9c7c")

BOT_TOKEN = getenv("BOT_TOKEN", "8023030133:AAHzuvmXz34QX8dV5utVo4Sg9lokWvZM13A")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1002881142866"))

OWNER_ID = int(getenv("OWNER_ID", "7926944005"))

BOT_USERNAME = getenv("BOT_USERNAME" , "gojo_x_jinwoobot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/itzarjuna1/SpyMusicxgojo",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "SPY")
GIT_TOKEN = getenv(
    "GIT_TOKEN", ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dark_x_knight_musiczz_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+3CTsVQWepswwY2Vk")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGbOzoAhG-dxyPz6hooGFhrmC2U_T5LNH-DV7SiFaHmaXbnDDhqg5Sticnf2Pi1FLktn0lrEeePxyIke64e8KJZThs8Mtc7Yx0eWDjRNdjkOeviRAVbYNP3dt6unOGtmzrvwB8gbV2vJevctK1U5rhj95ZiTAMtbCRAY0vWLt3mAyIdrPuXAjbclhJ72AWwkwx9W1Tbg2yk06xmzMSdqs43XX6Jnxf35GABkVPdx41nwAwMJemqjtIpnUnTH3TDnQu0RTbE2Uwvmlxp6C1LRLYESRsRS9Pkdrjeo1e3MfQP6Pto3-4pfkywhFlbVsnEbcDgo11k0Cy1ZC2WwqKVJdM8gQhwrwAAAAGsmbxnAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/4kpaiz.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/4kpaiz.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/4kpaiz.jpg"
STATS_IMG_URL = "https://files.catbox.moe/4kpaiz.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/928wbe.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/928wbe.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/928wbe.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/928wbe.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/928wbe.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/928wbe.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/928wbe.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/928wbe.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
