import os
import requests
import time

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=15
    )


def check(username):
    try:
        r = requests.get(
            f"https://www.instagram.com/{username}/",
            headers=HEADERS,
            timeout=15
        )

        if r.status_code == 404:
            return "not_found"

        if r.status_code == 200:
            return "found"

        return "unknown"

    except Exception:
        return "error"


with open("usernames.txt", encoding="utf-8") as f:
    usernames = [
        x.strip().lstrip("@")
        for x in f
        if x.strip()
    ]

for username in usernames:
    status = check(username)

    if status == "not_found":
        telegram(
            f"⚠️ Tekshirish kerak!\n\n"
            f"@{username}\n\n"
            f"Instagram'da qo'lda tekshiring."
        )

    time.sleep(3)
