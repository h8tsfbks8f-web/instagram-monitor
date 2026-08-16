import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=15
    )


with open("usernames.txt", encoding="utf-8") as file:
    usernames = [
        line.strip().lstrip("@")
        for line in file
        if line.strip()
    ]


for username in usernames:
    try:
        response = requests.get(
            f"https://www.instagram.com/{username}/",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15
        )

        if response.status_code == 404:
            send_message(
                f"⚠️ Tekshiring!\n\n"
                f"@{username}\n\n"
                f"Instagram'da qo'lda tekshirib ko'ring."
            )

    except requests.RequestException:
        pass
