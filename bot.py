# -*- coding: utf-8 -*-

import os
import random
from flask import Flask, request

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)

server = Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):

    with open("HELP.MD") as readme:
        readme_text = readme.read()
        bot.send_message(message.chat.id, readme_text, parse_mode="Markdown")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    
    if 'привет' in message.text.lower():
        greeting = "Ave!"
        bot.send_message(message.chat.id, greeting)

    else:
        bot.send_message(message.chat.id, 'Привет, Санёчек ;)')


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://cyber-caesar-bot.herokuapp.com/bot")
    return "!", 200


if __name__ == '__main__':
     # bot.polling(none_stop=True)

     server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
     server = Flask(__name__)
