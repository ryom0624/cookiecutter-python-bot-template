import json
from datetime import datetime
import logging
from os.path import dirname, join
from dotenv import load_dotenv

from {{cookiecutter.project_slug}}.notify import line
from {{cookiecutter.project_slug}}.logger import logger
from {{cookiecutter.project_slug}} import settings

def main():

    config = settings.init()
    log = logger.init(config)

    # ログ書き込みのタイミングを明示

    log.info("initializing....")
    log.info(
        "=================================================================="
    )
    log.info("{}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
    log.info(
        "===================================================================\n"
    )


if __name__ == "__main__":
    main()
