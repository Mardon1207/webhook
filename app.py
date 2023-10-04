from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler,MessageHandler,Filters
import handlers
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.environ.get('TOKEN')

print('TOKEN:', TOKEN)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, None, workers=0)


app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "webhook is running...!"
    
    if request.method == 'POST':
        
        body = request.get_json()
        
        update = Update.de_json(body, bot)

        dp.add_handler(CommandHandler(['start', 'boshlash'], handlers.start))
        dp.add_handler(MessageHandler(Filters.text("🐶DOG🐶"), handlers.dog))

        dp.process_update(update)

        return {'message': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)
