# Wallet Tracker Bot

Telegram бот для проверки баланса и мониторинга кошельков в блокчейне Solana. Баланс отображается в токенах и их долларовом эквиваленте. Можно единоразово посмотреть баланс кошелька или создать «ферму» кошельков и отслеживать её изменение с расчётом PNL

Поддержка других блокчейнов в разработке (сети EVM и Abstract)

## Стек технологий

- **Python 3.11+**
- **aiogram 3.x**
- **SQLAlchemy**
- **Alembic**
- **asyncpg**
- **PostgreSQL**
- **aiohttp**

## Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Darvinx2/Wallet_tracker_bot.git
cd Wallet_tracker_bot
```

### 2. Создай и активируй виртуальное окружение

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Создай файл переменных окружения

```bash
cp .env.example .env
```

Открой `.env` и заполни значения:

```
BOT_TOKEN=твой_токен_бота_от_BotFather
MORALIS_API_TOKEN=твой_ключ_moralis
DB_HOST=localhost
DB_PORT=5432
DB_NAME=SolanaCheckerBot
DB_USER=postgres
DB_PASSWORD=твой_пароль
```

### 5. Создай базу данных

Создай пустую базу данных с именем `SolanaCheckerBot` в PostgreSQL:

```bash
psql -U postgres -c "CREATE DATABASE \"SolanaCheckerBot\";"
```

### 6. Примени миграции

```bash
alembic upgrade head
```

### 7. Запусти бота

```bash
python main.py
```