import os


class Config(object):
    API_HASH = os.environ.get("1f5343b0646645ca1eaf7c4759fc248f")
    BOT_TOKEN = os.environ.get("6619594862:AAF7IMrryWmLpLnKDi-s8J41_u8YvbQHxm8")
    TELEGRAM_API = os.environ.get("26376042")
    OWNER = os.environ.get("2036803347")
    OWNER_USERNAME = os.environ.get("Sensei_Rimuru")
    PASSWORD = os.environ.get("AllInOne")
    DATABASE_URL = os.environ.get("mongodb+srv://userbot:userbot@cluster0.ltasu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001934076980")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
