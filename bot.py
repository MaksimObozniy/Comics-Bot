import os
import random
import requests
import asyncio
from aiogram.types import FSInputFile
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID") 
FILENAME = "comics.png"

bot = Bot(token=TOKEN)

def get_random_comic():
    latest = requests.get("https://xkcd.com/info.0.json").json()
    max_num = latest["num"]
    num = random.randint(1, max_num)
    url = f"https://xkcd.com/{num}/info.0.json"
    return requests.get(url).json()

async def send_comic():
    comic = get_random_comic()
    img_url = comic["img"]
    caption = comic["alt"]

    img_data = requests.get(img_url).content
    with open(FILENAME, "wb") as f:
        f.write(img_data)

    input_file = FSInputFile(FILENAME)  # <-- правильный способ
    await bot.send_photo(chat_id=CHAT_ID, photo=input_file, caption=caption)

    os.remove(FILENAME)

async def scheduler():
    while True:
        await send_comic()
        await asyncio.sleep(60 * 30)

async def main():
    await scheduler()

if __name__ == "__main__":
    asyncio.run(main())
