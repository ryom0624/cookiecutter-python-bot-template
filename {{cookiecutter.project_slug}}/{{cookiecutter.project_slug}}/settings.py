import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

PATH = "./"
ENV_DIR = "../"

def init():

    # ==========================================================
    # init
    # ==========================================================
    config = json.load(open(PATH + "config.json", "r"))

    load_dotenv(verbose=True)
    dotenv_path = join(dirname(__file__), ENV_DIR + ".env")
    load_dotenv(dotenv_path)

    return config
