from datetime import datetime
from logging import DEBUG, INFO, Formatter, StreamHandler, getLogger
from os.path import dirname, join
import logging.handlers


def init(config):
    # ==========================================================
    # ログの設定
    # ==========================================================
    logger = getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # handlerで複数のloggerを使い分けることができる。
    # 標準出力
    logHandler = StreamHandler()
    logHandler.setLevel(DEBUG)
    logHandler.setFormatter(
        Formatter("%(levelname)-5s [%(asctime)s.%(msecs)-3d] %(message)s",
            datefmt="%Y/%m/%d %H:%M:%S",
        )
    )

    # ファイル出力
    logFileHandler = logging.handlers.TimedRotatingFileHandler(
        filename="{}/{}.log".format(config["LOGGING_DIR"], datetime.now().strftime("%Y%m%d%H%M%S")),
        backupCount=config["LOGGING_LOTATION_COUNT"],
        when="MIDNIGHT",
        encoding="UTF-8",
    )
    logFileHandler.setLevel(INFO)
    logFileHandler.setFormatter(
        Formatter(
            "%(levelname)-5s [%(asctime)s.%(msecs)-3d] %(message)s",
            datefmt="%Y/%m/%d %H:%M:%S",
        )
    )

    logger.addHandler(logHandler)
    logger.addHandler(logFileHandler)

    return logger
