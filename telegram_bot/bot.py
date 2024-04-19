import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,ApplicationBuilder
from dotenv import load_dotenv

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello from django telegram bot !')

def main() -> None:
    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
    logger = logging.getLogger(__name__)
    load_dotenv()
    token = os.getenv('TOKEN')
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()
