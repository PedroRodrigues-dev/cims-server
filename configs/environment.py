import os


def serverName():
    return os.getenv("CIMS_SERVER_SERVER_NAME")


def systemTimeout():
    return os.getenv("CIMS_SERVER_SYSTEM_TIMEOUT") or 5


def rabbitUsername():
    return os.getenv("CIMS_SERVER_RABBIT_USERNAME") or "guest"


def rabbitPassword():
    return os.getenv("CIMS_SERVER_RABBIT_PASSWORD") or "guest"


def rabbitHost():
    return os.getenv("CIMS_SERVER_DISCORD_RABBIT_HOST") or "localhost"
