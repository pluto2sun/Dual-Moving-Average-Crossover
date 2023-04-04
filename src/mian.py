from loguru import logger
from retrying import retry
from ..url.url_formats import (buff_json_fmt, c5_json_fmt, igxe_json_fmt,
                         order_json_fmt, uuyp_json_fmt, volume_json_fmt)

logger.add('../log/main.log', enqueue=True, rotation='1 MB', backtrace=True, diagnose=True)

game_info = [
    {'game': 'csgo',  'appid':730},
    {'game': 'dota2', 'appid':570},
]

if __name__ == '__main__':
    logger.info("Start to fetch main info ...")
    print("")