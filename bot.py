from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext ):
    update.message.reply_text('Hola, humano!')


def getPrice(update: Update, context: CallbackContext ):
    update.message.reply_text('El precio es: 1000')