# Comics Bot

Telegram-бот, автоматически публикующий случайные комиксы из xkcd в Telegram-канал каждые 30 минут.


## Enviroment

```bash
python -m venv .venv #Для всех ОС

#run enviroment
.venv\Scripts\activate #для Windows
source .venv/bin/activate #для Linux/MacOS
```


### Requirements

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```


### Enviroment variables

- BOT_TOKEN

- CHAT_ID

1. Поместите файл `.env` рядом с `bot.py`.

2. `.env` содержит текстовые данные без кавычек.

Например, если вы распечатаете содержимое `.env`, вы увидите:
```bash
$ cat .env
TG_BOT_TOKEN=1946382059:AAF-dhk_M2OiQXVTnbU-lIwBRqcrWKszXWk
TG_CHAT_ID=-1008492606231 #или же @name_bot
```


#### How to get

BOT_TOKEN можно получить при создании бота через @BotFather, он выглядит примерно вот так:
```bash
1946382059:AAF-dhk_M2OiQXVTnbU-lIwBRqcrWKszXWk
```
CHAT_ID это ID вашего канала куда будет выкладываться комикс, он выглядит примерно вот так:

```bash
-1008492606231
#или так:
@name_bot
```


## Run

```bash
python bot.py
```

После всех выполненных условий, вы можете увидеть в своет телеграм канале автоматически публикуются посты с промежутком в 30 минут.


## Project Goals

Код написан в образовательных целях. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org).