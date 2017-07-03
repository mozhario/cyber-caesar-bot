# -*- coding: utf-8 -*-

import random

import config
import telebot


bot = telebot.TeleBot(config.TOKEN)


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


if __name__ == '__main__':
     bot.polling(none_stop=True)
