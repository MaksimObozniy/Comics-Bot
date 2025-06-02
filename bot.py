import os
import time
import random
import requests
from telegram import Bot
from dotenv import load_dotenv


def get_random_comic():
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()
    latest_comic = response.json()
    max_num = latest_comic["num"]
    num = random.randint(1, max_num)
    url = f"https://xkcd.com/{num}/info.0.json"
    response_url = requests.get(url)
    response_url.raise_for_status()
    return response_url.json()


def download_image(img_url, filename):
    response = requests.get(img_url)
    response.raise_for_status()
    img_content = response.content
    with open(filename, "wb") as f:
        f.write(img_content)


def send_comic(filename, chat_id, bot, caption):
    with open(filename, 'rb') as image:
        bot.send_photo(chat_id=chat_id, photo=image, caption=caption)


def main():
    load_dotenv()

    tg_token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    filename = "comics.png"

    bot = Bot(token=tg_token)

    while True:
        comic = get_random_comic()
        img_url, caption = comic['img'], comic['alt']
        download_image(img_url, filename)
        try:
            send_comic(filename, chat_id, bot, caption)
        finally:
            if os.path.exists(filename):
                os.remove(filename)
        time.sleep(60 * 30)


if __name__ == "__main__":
    main()
