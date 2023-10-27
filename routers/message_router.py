#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aiogram import F, Router
from handlers.message_handler import *

router = Router()
router.message.filter(F.chat.type == "private")

handlers = {
    keyboard_words[0]: subscription_handler,
    keyboard_words[1]: new_word_handler,
    keyboard_words[2]: settings_handler,
    keyboard_words[3]: test_handler,
    keyboard_words[4]: get_help_handler,
    keyboard_words[5]: statistics_handler,
}


@router.message(F.text)
async def extract_data(message: types.Message) -> None:
    with SqlActions('users') as sql_user:
        user_data = sql_user.sql_query(chat_id=message.from_user.id)

    if not user_data or not all(user_data[0][3:5]):
        return
    if message.text in handlers:
        await handlers[message.text](user_data, message)
    elif len(message.text) < 50:
        await other_words_handler(user_data, message)
    else:
        await message.answer(uk_dict['too_long_text'])
