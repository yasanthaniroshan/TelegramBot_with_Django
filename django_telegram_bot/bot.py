import os,django
from django_telegram_bot.settings import DATABASES,INSTALLED_APPS
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_telegram_bot.settings')
django.setup()
from asgiref.sync import sync_to_async
from user_data.models import UserData
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,ApplicationBuilder
from dotenv import load_dotenv

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    try:
        user_data = await sync_to_async(UserData.objects.get)(id=user_id)
        await update.message.reply_text(f'Welcome back {user_data.first_name}!')
    except UserData.DoesNotExist:
        new_user = UserData(id=user_id, first_name=update.effective_user.first_name, last_name=update.effective_user.last_name, username=update.effective_user.username)
        await sync_to_async(new_user.save)()
        logging.info(f'New user {new_user.first_name} has been added to the database')
        await update.message.reply_text('Welcome to django-telegram-bot!')

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

if __name__ == '__main__':
    main()
