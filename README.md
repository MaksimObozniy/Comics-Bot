# Comics Bot

Telegram-бот, автоматически публикующий случайные комиксы из xkcd в Telegram-канал каждые 30 минут.

## Возможности

- Загружает случайный комикс с сайта xkcd
- Отправляет изображение и описание в Telegram-канал
- Интервал публикации — 30 минут


## Установка

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/yourusername/Comics-Bot.git
   cd Comics-Bot
   ```

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate #Запуск виртуального окружения
   # или
   source .venv/bin/activate  
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создать файл `.env` с переменными:

   ```env
   BOT_TOKEN=ваш_токен_бота
   CHAT_ID=@ваш_канал
   ```

   BOT_TOKEN можно получить при создании бота через @BotFather
   CHAT_ID это ID вашего канала куда будет выкладываться комикс


5. Запустить скрипт:

   ```bash
   python bot.py
   ```
