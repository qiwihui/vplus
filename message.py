# coding: utf-8
import datetime
import sys
from pathlib import Path
from telegram import Bot
import config


def send_telegram_message(
    message: str, chat_id=config.TELEGRAM_CHAT_ID, token=config.TELEGRAM_SENDER_TOKEN
) -> None:

    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message)


if __name__ == "__main__":
    state = sys.argv[1]
    if Path("result.txt").exists():
        with open("result.txt", "r") as f:
            send_telegram_message(f.read())
    else:
        send_telegram_message(f"{state} @ " + str(datetime.datetime.now()))
