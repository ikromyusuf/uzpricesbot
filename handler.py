from telegram.ext import CommandHandler

from bot import start

def addHandlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))

    return dispatcher