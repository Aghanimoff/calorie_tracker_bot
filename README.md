# Calorie Tracker Bot

Calorie Tracker Bot — это Telegram бот для ежедневного учета потребления калорий и физической активности пользователей.

## Особенности

- Запрос у пользователя информации о рационе и физической активности за предыдущий день.
- Анализ данных с использованием API ChatGPT.
- Сохранение и учет данных в базе данных SQLite.

## Требования

Для работы проекта вам понадобится Python 3.6 или выше. Все зависимости перечислены в файле `requirements.txt`.

## Установка

1. Клонируйте репозиторий проекта:
   ```
   git clone https://github.com/Aghanimoff/calorie_tracker_bot
   cd calorie_tracker_bot
   ```

2. Создайте виртуальное окружение и активируйте его:
   ### Для Windows
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
   ### Для MacOS/Linux
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Установите необходимые библиотеки:
   ```
   pip install -r requirements.txt
   ```

## Настройка

1. Получите токены:
   - **Токен Telegram**: Создайте бота в Telegram через [BotFather](https://t.me/botfather) и получите токен.
   - **API ключ OpenAI**: Зарегистрируйтесь на [OpenAI](https://www.openai.com/), создайте новое приложение и получите API ключ.

2. Настройте переменные окружения. Создайте файл `.env` в корневой директории проекта и добавьте следующее:
   ```
   TELEGRAM_API_TOKEN='ваш_токен_телеграм'
   OPENAI_API_KEY='ваш_openai_api_ключ'
   ```

   Или настройте переменные окружения в вашей системе:
   ### Для Windows
   ```
   set TELEGRAM_API_TOKEN=ваш_токен_телеграм
   set OPENAI_API_KEY=ваш_openai_api_ключ
   ```
   ### Для MacOS/Linux
   ```
   export TELEGRAM_API_TOKEN=ваш_токен_телеграм
   export OPENAI_API_KEY=ваш_openai_api_ключ
   ```

3. Создайте базу данных и инициализируйте структуру:
   ```
   python -c 'from database.models import create_db; create_db()'
   ```

## Запуск

Запустите бота с помощью следующей команды:
```
python bot/main.py
```

Бот будет автоматически запускаться и ожидать сообщений от пользователей.

## Разработка

Для добавления новых функций или изменения текущих, модифицируйте файлы в соответствующих директориях:
- `bot/` для логики Telegram бота.
- `database/` для работы с базой данных.
- `utils/` для вспомогательных утилит.
