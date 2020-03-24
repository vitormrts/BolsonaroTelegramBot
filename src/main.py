from telegram import Bot, Update

from time import sleep

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, Dispatcher

import os

import re


def teste_callback(bot, update):

    auth = tweepy.OAuthHandler('id9ZkfAAQf2CAFAPZfuJR8Oot', 'Gumun9JsIkKg2orIpzk1ckCqsax8FxhzJxwuos4W14ZoFZxONw')
    auth.set_access_token('2982469253-jhBGYBWFh9ev3qiYEVXbVEOozTaOXGYxv4yI2QQ','yCeNDCgLR1Zhcwqfht40ZRncxSpLA2yLoBeaJP3Y9igBq')


    api = tweepy.API(auth)


    def obter_tweets(usuario, limite=1):
        resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended')
        tweets = []
        for r in resultados:
            tweet = re.sub(r'http\S+', '', r.full_text)
            tweets.append(tweet.replace('\n', ' '))
        return tweets


    tweets = obter_tweets(usuario='jairbolsonaro', limite=1)


    def msg(bot, update):
        update.message.reply_text(tweets, quote=False)


def danca_callback(bot, update):
    bot.sendAnimation(
        chat_id=update.message.chat_id,
        animation="https://media.giphy.com/media/dsQrhW15qfUhWjjVMl/giphy.gif"
    )

def gado_callback(bot, update):
    bot.sendAnimation(
        chat_id=update.message.chat_id,
        animation="https://media.tenor.com/images/4ab2e1d37b5d71289796677692748605/tenor.gif"
    )


def coronavirus_callback(bot, update):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo="https://pbs.twimg.com/media/ETZdc34WkAEA2Fh.jpg"
    )
    sleep(0.8)
    response_message = "Talquei?! >:("
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def pt_callback(bot, update):
    bot.sendAnimation(
        chat_id=update.message.chat_id,
        animation="https://media.tenor.com/images/ec30360d8edca1ea94b7476508d8f67d/tenor.gif"
    )


def unknown_callback(bot, update):
    response_message = "Eu não sei esse comando, mas e o PT?\nTambém não sabe né?!\nTalquei"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def webhook(request):

    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

    dispatcher = Dispatcher(bot, None, 0)


    dispatcher.add_handler(CommandHandler('pt', pt_callback))
    dispatcher.add_handler(CommandHandler('faloumerda', teste_callback))
    dispatcher.add_handler(CommandHandler('danca', danca_callback))
    dispatcher.add_handler(CommandHandler('coronavirus', coronavirus_callback))
    dispatcher.add_handler(CommandHandler('gado', gado_callback))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown_callback))
    if request.method == 'POST':
        contador_faloumerda = 0
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'
