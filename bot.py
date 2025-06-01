import os
import random
import requests
import asyncio
from aiogram.types import FSInputFile
from aiogram import Bot
from dotenv import load_dotenv


def get_random_comic():
    latest = requests.get("https://xkcd.com/info.0.json").json()
    max_num = latest["num"]
    num = random.randint(1, max_num)
    url = f"https://xkcd.com/{num}/info.0.json"
    return requests.get(url).json()


def download_image(url, filename):
    img_data = requests.get(url).content
    with open(filename, "wb") as f:
        f.write(img_data)


async def send_comic(filename, chat_id, bot):
    comic = get_random_comic()
    img_url = comic["img"]
    caption = comic["alt"]

    download_image(img_url, filename)
    
    input_file = FSInputFile(filename)
    
    try:
        await bot.send_photo(chat_id=chat_id, photo=input_file, caption=caption)
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def main():
    load_dotenv()

    tg_token = os.getenv("TG_BOT_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    filename = "comics.png"

    bot = Bot(token=tg_token)

    async def scheduler():
        while True:
            await send_comic(filename, chat_id, bot)
            await asyncio.sleep(60 * 30)

    asyncio.run(scheduler())


if __name__ == "__main__":
    main()
