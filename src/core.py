from time import sleep

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from src.conf.settings import BASE_API_URL, TELEGRAM_TOKEN




def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def bolsonaro_falou_merda(bot, update):
    #contadorbolsonaromerda += 1
    #mensagem_falou_merda()
    response_menssage = 'O Bonoliro falou merda? '
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_menssage
    )

def mensagem_falou_merda():
    print('O Bonoliro falou merda?')
    sleep(0.5)
    print('SIM!')
    sleep(0.5)
    print('Quantas vezes?')
    sleep(0.4)


def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=BASE_API_URL + args[0]
    )


def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        CommandHandler('faloumerda', bolsonaro_falou_merda)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()