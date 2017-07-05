# -*- coding: utf-8 -*-

import os
import random
import requests
import json
from flask import Flask, request

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)

server = Flask(__name__)


def strip_command(text):
    return " ".join(text.split(' ')[1:])


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):

    with open("HELP.MD") as readme:
        readme_text = readme.read()
        bot.send_message(message.chat.id, readme_text, parse_mode="Markdown")


@bot.message_handler(commands=['encrypt'])
def handle_encrypt(message):
    inpt = strip_command(message.text)
    params = inpt.split("#")
    text = params[0]
    key = params[1]

    resp = requests.get("https://cybercaesar.herokuapp.com/encrypt/", params={"original_text": text, "rotation": key})

    resp = resp.json()

    bot.send_message(message.chat.id, resp["encrypted"])


@bot.message_handler(commands=['decrypt'])
def handle_encrypt(message):
    inpt = strip_command(message.text)
    params = inpt.split("#")
    text = params[0]
    key = params[1]

    resp = requests.get("https://cybercaesar.herokuapp.com/decrypt/", params={"encrypted_text": text, "rotation": key})

    resp = resp.json()

    bot.send_message(message.chat.id, resp["decrypted"])


@bot.message_handler(commands=['break'])
def handle_decrypt(message):
    inpt = strip_command(message.text)

    resp = requests.get("https://cybercaesar.herokuapp.com/break-cipher/", params={"text": inpt})

    resp = resp.json()
    msg_text = "key: %d \nDecrypted text: %s" % (resp["key"], resp["decrypted"])

    bot.send_message(message.chat.id, msg_text)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    
    if 'hello' in message.text.lower():
        greeting = "Ave!"
        bot.send_message(message.chat.id, greeting)

    else:
        quote = random.choice(config.CAESAR_QUOTES)
        bot.send_message(message.chat.id, quote)


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.WEBHOOK_URL)
    return "!", 200


if __name__ == '__main__':
     # bot.polling(none_stop=True)

     server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
     server = Flask(__name__)
