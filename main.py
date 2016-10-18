# -*- coding: utf-8 -*-
# ! /usr/bin/env python

import logging
import requests
import sys
import random

from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters)

from config import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Buenas, ¿ya venís a dar por culo al bar?')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text="""Mario Bot v1.0:
Me encargo de poner orden en la BOFHcueva y de proporcionar alcoholes varios.
                    """)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def randomchat(bot, update):
    msg = update.message.text.lower()
    user_name = update.message.from_user.username.lower()
    replies = []

    if "as a service" in msg:
        replies.append(random.choice([
            "Que no te hoygan en Stratio",
            "Lo desplegaremos con Docker",
            "Eso se hace con Mesos en dos patadas",
            "No tiene suficiente hype",
        ]))

    if "la rusa" in msg:
        replies.append(random.choice([
            "Ahora te daré la brasa con un parche mío en Github.",
            "Eso en Javascript va 183452345342 millones de veces más rápido.",
            "SystemD es nuestro señor y salvador, haters de mierda.",
            "Me jode mucho que Reset me haya programado en Python.",
        ]))

    if "datio" in msg:
        replies.append("¡ah!, ¿ya existe Datio?")

    if "maiesekueleh" in msg:
        replies.append(random.choice([
            "XRO HASEJURATE DE KE HES LA HENTEPRAIS KORPRORATE HEDISION KRAKEADA.",
            "HOYGAN VOFERS, PACENME LA HULTIMA BERSION.",
            "MUSHO MEGOR KE LA MONGERDEVE HESA RARA.",
            "HOYGAN KOMO ME LO HINZTALO EN MI JUINDOUZ ENETE?"
        ]))

    if "peachepe" in msg:
        replies.append(random.choice([
            "XRA AZER JUEBS DE HEXKANDALO KRAKEADO PRIMIAM POFREZIONAL HEDISHION",
            "HOYGAN KE NO ME KOMPILA MI KODIJO PEACHEPE HALLUDENME",
            "LLO HUSO TAMVIEN EL MEGOR LENJUAGUE DEL MUNDO",
            "NO PUEDO HINZTALARLO EN MI JAMEVOY HALLUDA"
        ]))

    if "puto bot" in msg and "martixx" in user_name:
        replies.append("HOYGA, punki, no se pase un pelo")

    if "linux" in msg and "gnu/linux" not in msg and "gnu linux" not in msg and "gnu\linux" not in msg:
        replies.append("GNU/Linux, por favor. Linux es sólo el kernel")

    if len(replies) > 0:
        if len(replies) > 5:
            reply = random.choice(["Sois unos pesaos", "java.lang.IndexOutOfBoundsException",
                                   "A ve, vamos por partes. Peazo de trolles",
                                   "Ahora me enfado y no respiro. Pesaos."])
            bot.sendMessage(update.message.chat_id, text=reply)
        else:
            bot.sendMessage(update.message.chat_id, text=random.choice(replies))


def buscar(bot, update, args):
    duck_url = "http://api.duckduckgo.com"

    params = {"q": " ".join(args), "format": "json", "no_html": 1, "skip_disambig": 1}
    query = requests.get(duck_url, params=params)
    if len(query.json().items()) > 0:
        result = ""
        if query.json()["Infobox"] != "":
            for element in query.json()["Infobox"]["content"]:
                result += element["label"] + ": " + element["value"] + "\n"

        else:
            result = "No he encontrado nada, sigue rascando"

    else:
        result = "Tango Down: El pato de las búsquedas está caído."

    bot.sendMessage(update.message.chat_id, text=result)


def main():
    token = config.get('TOKEN')

    if token is None:
        print("Please, configure your token first")
        sys.exit(1)

    updater = Updater(token)
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("buscar", buscar, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler([Filters.text], randomchat))

    # log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    print("Starting MarioBot")
    main()
