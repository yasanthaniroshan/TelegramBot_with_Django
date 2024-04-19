# Telegram Bot with Django

This project is a Telegram bot built using Django framework. The bot has several features of DjangoORM integrated with Telegram API.

## Installation

1. Clone the repository : 
    ```bash
    git clone https://github.com/your-username/TelegramBot_with_Django.git`
    ```
2. Install the required dependencies : 
    ```bash
    cd TelegramBot_with_Django
    pip install -r requirements.txt
    ```
3. Get the Telegram API token and add it to the .env file.
    ```bash
    Token=your-telegram-bot-token
    ```
4. Populate the database with the initial data.
    ```bash
    cd django_telegram_bot
    python manage.py makeinitialmigrations
    python manage.py migrate
    ```
5. Start bot by running bot.py file.
    ```bash
    python bot.py
    ```
## Usage

1. Start the Telegram bot by running above commands.
2. Open Telegram and search for your bot.
3. Start a conversation with the bot and use the available commands.

## Contributing

Contributions are welcome! If you have any ideas or suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).