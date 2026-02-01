Telegram бот для проверки баланса и мониторинга его изменений для кошелька(ов) в блокчейне Solana, баланс отображается в токенах и их долларовом эквиваленте
Можно как единоразово посмотреть баланс кошелька, так и создать "ферму" кошельков и отслеживать ее изменение с расчетом PNL
Поддержка других блокчейнов в разработке (в частности сетей EVM и Abstract)


## Используемый стек технологий

- **Python 3.11+**
- **aiogram 3.x**
- **PostgreSQL**
- **asyncpg**
- **aiohttp**


### Установка

**1. Клонируй репозиторий:**
```bash
git clone https://github.com/Darvinx2/Wallet_tracker_bot.git
cd Wallet_tracker_bot
```

**2. Создай и активируй виртуальное окружение:**
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Установи зависимости:**
```bash
pip install -r requirements.txt
```

**4. Создай файл переменных окружения:**
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

**5. Создай таблицы в базе данных:**

Создай новую БД с именем `SolanaCheckerBot` в PgAdmin, затем открой файл `database/schema.sql` и выполни его

Или через psql:
```bash
psql -U postgres -d SolanaCheckerBot -f database/schema.sql
```

**6. Запусти бот:**
```bash
python main.py
```