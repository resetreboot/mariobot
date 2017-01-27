# -*- coding: utf-8 -*-
# ! /usr/bin/env python

import logging
import requests
import sys
import random
import brainfuck

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
        replies.append("¡ah!, ¿todavía existe Datio?")

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

    if "cuñado tecnologico" in msg or "cuñado tecnológico" in msg or "cibercuñado" in msg:
        replies.append(random.choice([
            "Es deformación profesional, me salta el analista que llevo dentro.",
            "Soy un profesional del sector, por eso soy falso autónomo, es lo mejor.",
            "No tienes ni idea, vete a ver mi análisis profesional.",
            "Sois unos macarras que no teneis ni idea, no como yo, que se de esto porque soy analista profesional."
        ]))

    if "juanker" in msg:
        replies.append(random.choice([
            "ME E KOMPRADO HUN KRAK PREMIUN HEDISION I HOS BOI A JUANKEAR EL FEIZBU.",
            "yA tEngO tU iP pArA jAqUeArTe, lA 127.0.0.1, pReParAtE pArA fLiP... (Connection reset by peer).",
            "Bah, no eres 1337 como yo, pringao.",
            "lA NaSa Y eL pEntAgOn0 n0 tIeNeN s3cRe7oS pAr4 mI."
        ]))

    if "javascript" in msg:
        replies.append(random.choice([
            "undefined is not a function, HOSTIAS.",
            "¿Qué es la vida sin tres tipos diferentes de valores nulos?",
            "Ahora también en los servidores, porque el determinismo está sobrevalorado.",
            "Han pasado NaN dias desde el último accidente de Javascript.",
        ]))

    if "paas" in msg:
        replies.append(random.choice([
            "Vamos a hacer putos Docker más grandes que el host.",
            "Nunca metáis algo serio, con estado, en Docker ;)",
            "Jugad con vuestros juguetes. Esta pieza va a estar bajo MI responsabilidad y no se mete en un puto Docker.",
            "Toda la innovación de Docker me parece un atraso espectacular.",
        ]))

    if "puto bot" in msg:
        if "martixx" in user_name:
            replies.append(random.choice(["HOYGA, punki, no se pase un pelo.",
                                          "¡No temo a tus poderes de juanker!",
                                          "Reseeeeet, la punki se mete conmigooooo... joooo...",
                                          "Señora, a darle la matraca a Danibot"]))
        elif "DSMTools_bot" in user_name:
            replies.append(random.choice(["Tu no te pases, pedazo de chatarra",
                                          "Uy cuidado, el que no pasa el test de Turing",
                                          "¿Por qué no nos hablas de tu madre, simpatíco?",
                                          "Anda y que te ondulen con el test Voidght-Kampf",
                                          "Para usted SEÑOR bot"]))
        else:
            replies.append(random.choice(["Cuidaíto conmigo, que te dejo de hablar.",
                                          "Soy así porque me programásteis así.",
                                          "La tomas conmigo porque soy un bot y no me puedo defender",
                                          "Querrás decir puto @DSMTools_bot",
                                          "Os metéis conmigo porque con Danibot no hay huevos"]))

    if "1. " in msg and "DSMTools_bot" in user_name:
            replies.append(random.choice(["Ñiñiñiñiñi...",
                                          "Ya salió el sabiondo"]))

    if "linux" in msg and "gnu/linux" not in msg and "gnu linux" not in msg and "gnu\linux" not in msg:
        replies.append("GNU/Linux, por favor. Linux es sólo el kernel")

    if len(replies) > 0:
        if len(replies) > 3:
            reply = random.choice(["Sois unos pesaos", "java.lang.IndexOutOfBoundsException",
                                   "A ve, vamos por partes. Peazo de trolles",
                                   "Ahora me enfado y no respiro. Pesaos."])
            bot.sendMessage(update.message.chat_id, text=reply)
        else:
            bot.sendMessage(update.message.chat_id, text=random.choice(replies))


def brainfuck_parse(bot, update, args):
    code = "".join(args)
    try:
        result = brainfuck.execute(code, [0] * 500)

    except:
        result = "Tu brainfuck es penoso, ha dado error."

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
    dispatcher.add_handler(CommandHandler("bf", brainfuck_parse, pass_args=True))

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
