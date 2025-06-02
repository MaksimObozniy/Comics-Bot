import os
import time
import random
import requests
from telegram import Bot
from dotenv import load_dotenv


def get_random_comic():
    latest = requests.get("https://xkcd.com/info.0.json").json()
    max_num = latest["num"]
    num = random.randint(1, max_num)
    url = f"https://xkcd.com/{num}/info.0.json"
    return requests.get(url).json()


def get_comic_image_and_caption():
    comic = get_random_comic()
    return comic['img'], comic['alt']


def download_image(img_url, filename):
    img_data = requests.get(img_url).content
    with open(filename, "wb") as f:
        f.write(img_data)

    
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


def send_comic(filename, chat_id, bot, caption):
    try:
        with open(filename, 'rb') as image:
            bot.send_photo(chat_id=chat_id,
                           photo=image,
                           caption=caption)
    finally:
        remove_file(filename)


def main():
    load_dotenv()

    tg_token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    filename = "comics.png"

    bot = Bot(token=tg_token)

    while True:
        img_url, caption = get_comic_image_and_caption()
        download_image(img_url, filename)
        send_comic(filename, chat_id, bot, caption)
        time.sleep(5)


if __name__ == "__main__":
    main()
