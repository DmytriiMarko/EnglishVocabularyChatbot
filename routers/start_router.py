#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aiogram.filters import CommandStart
from aiogram import Router, F
from handlers.start_handler import *
from database import *


router = Router()
router.message.filter(F.chat.type == "private")


@router.message(CommandStart())
async def process_start_command(message: types.Message) -> None:
    user_id = message.from_user.id

    with SqlActions('users') as sql_user:
        user_data = sql_user.sql_query(chat_id=user_id)

    if not user_data or not all(user_data[0][3:5]):
        await handle_new_user(message)
    else:
        await handle_existing_user(message)
