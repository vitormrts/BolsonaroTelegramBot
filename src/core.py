from time import sleep

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from src.conf.settings import BASE_API_URL, TELEGRAM_TOKEN

import emoji

def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def faloumerda_callback(bot, update, **optional_args):
    global contador_faloumerda

    contador_faloumerda += 1

    update.message.reply_text(
        "O Bonoliro falou merda?",
        quote=False)

    sleep(0.5)

    update.message.reply_text(
        "SIM!",
        quote=False
    )

    sleep(0.5)

    update.message.reply_text(
        "Quantas vezes?",
        quote=False
    )

    sleep(0.5)

    update.message.reply_text(contador_faloumerda, quote=False)

    if contador_faloumerda%13 == 0:
       update.message.reply_text(
           emoji.emojize(f"{contador_faloumerda}? {contador_faloumerda} é múltiplo de 13 :rage:", use_aliases=True)
       ),
       update.message.reply_text(
            emoji.emojize("Culpa do PT, talquei?! :sunglasses: ", use_aliases=True)
        )
def coronavirus_callback(bot, update):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=BASE_API_URL
    )

    sleep(0.5)

    update.message.reply_text(
        emoji.emojize('Talquei?! :sunglasses: :triumph:   ', use_aliases=True), quote=False
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
        CommandHandler('coronavirus', coronavirus_callback)
    )
    dispatcher.add_handler(
        CommandHandler('faloumerda', faloumerda_callback)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    contador_faloumerda = 12
    main()