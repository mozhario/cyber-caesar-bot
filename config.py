# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_env_variable(var_name):
    try:
        return os.getenv(var_name)
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise KeyError(error_msg)


# telegram token
TOKEN = get_env_variable("CAESAR_TG_TOKEN")

CAESAR_API_URL = "https://cybercaesar.herokuapp.com/"

CAESAR_QUOTES = (
    'Veni, vidi, vici.',
    'I came, I saw, I conquered.',
    'The die is cast.',
    'Sed fortuna, quae plurimum potest cum in reliquis rebus tum praecipue in bello, parvis momentis magnas rerum commutationes efficit; ut tum accidit.',
    'Fortune, which has a great deal of power in other matters but especially in war, can bring about great changes in a situation through very slight forces.',
    'I assure you I had rather be the first man here than the second man in Rome.',
    'Alea iacta est.'
)