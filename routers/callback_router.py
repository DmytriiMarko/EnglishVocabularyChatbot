#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aiogram import F, Router
from handlers.callback_handler import *

router = Router()

handlers = {
    "get_voice": get_voice_handler,
    "LVL": select_level_handler,
    "NOT": select_notification_handler,
    "HIDE": select_hide_handler,
    "TEST": complete_test_handler,
    "SET": edit_settings_handler,
    "learned": word_status_handler,
    "not_learned": word_status_handler,
    "learn_again": word_status_handler,
    "have_learned": learning_status_handler,
    "have_learned_yes": learning_status_handler,
    "not_learned_no": not_learned_handler
}


@router.callback_query(F.data)
async def json_box(query: types.CallbackQuery):
    with SqlActions('users') as sql_user:
        user_data = sql_user.sql_query(chat_id=query.message.chat.id)

    if not user_data:
        return

    for key, handler in handlers.items():
        if query.data.startswith(key):
            await handler(user_data, query)
            break
