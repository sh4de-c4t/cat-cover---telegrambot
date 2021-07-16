
from forwardscoverbot import constants

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def github_link_kb():
    button0 = InlineKeyboardButton(
            text="My Channel", 
            url="t.me/Radio_deev")
    buttons_list = [[button0]]
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard


def private_chat_kb():
    bot_link = "https://t.me/{}".format(constants.GET_ME.username)
    button0 = InlineKeyboardButton(text="Private chat", url=bot_link)
    buttons_list = [[button0]]
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard
