from telegram import Update,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import CallbackContext
import requests


def start(update: Update, context: CallbackContext):
    keyboards = [
        [KeyboardButton('🐶DOG🐶')]
    ]
    update.message.reply_text(
        text='Hello!, welcome to bot!',
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
    )
    return 
def dog(update: Update, context: CallbackContext):
    URL="https://random.dog/woof.json"
    response=requests.get(URL)
    a=response.json()
    context.bot.sendPhoto(update.message.chat.id,a['url'])
