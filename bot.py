from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
import handlers
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.environ.get('TOKEN')


def main():
    updater = Updater(token=TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(Filters.text("🐶DOG🐶"), handlers.dog))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    