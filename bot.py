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

async def send_comic(filename, tg_chat_id, bot):
    comic = get_random_comic()
    img_url = comic["img"]
    caption = comic["alt"]

    img_data = requests.get(img_url).content
    with open(filename, "wb") as f:
        f.write(img_data)

    input_file = FSInputFile(filename)
    await bot.send_photo(chat_id=tg_chat_id, photo=input_file, caption=caption)
    
    os.remove(filename)

def main():
    load_dotenv()
    
    tg_token = os.environ("TG_BOT_TOKEN")
    tg_chat_id = os.environ("TG_CHAT_ID") 
    filename = "comics.png"
    
    bot = Bot(token=tg_token)
    
    async def scheduler():
        while True:
            await send_comic(filename, tg_chat_id, bot)
            await asyncio.sleep(60 * 30)

    asyncio.run(scheduler())

if __name__ == "__main__":
    main()
