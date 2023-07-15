from telegram.ext import Updater

from handler import addHandlers

# get token from env
import os
token = os.environ.get('TOKEN')

if __name__ == '__main__':
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher = addHandlers(dispatcher)

    updater.start_polling()
    updater.idle()