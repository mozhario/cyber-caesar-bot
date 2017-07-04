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