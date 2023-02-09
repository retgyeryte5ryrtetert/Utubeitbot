import os


class Config:

    BOT_TOKEN = os.environ.get("5822649738:AAEbSEWPhTBW0WjbzvdIPB1ZHawMU66VVq0")

    SESSION_NAME = ":memory:"

    API_ID = int(os.environ.get("25598620"))

    API_HASH = os.environ.get("2efd1241218b944bd44bc08eb096276d")

    CLIENT_ID = os.environ.get("905151919387-nrboqgg068p5pckvloo58jgbj4gsehcr.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("5962397317"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
