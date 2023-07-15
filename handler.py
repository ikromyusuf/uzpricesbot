from telegram.ext import CommandHandler

from bot import start, getPrice

def addHandlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('kungaBoqarYogi', getPrice))

    return dispatcher