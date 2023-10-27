#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aiogram import types
from utils import uk_dict
from keyboards import choose_level_keyboard, greeting_keyboard
from database import *


async def handle_new_user(message: types.Message) -> None:
    user_id = message.from_user.id
    await message.answer(text=uk_dict['greeting'])

    with SqlActions('users') as sql_user:
        sql_user.sql_insert(chat_id=str(user_id))

    await message.answer(text=uk_dict['question_1'], reply_markup=choose_level_keyboard)


async def handle_existing_user(message: types.Message) -> None:
    await message.answer(text=uk_dict['greeting'], reply_markup=greeting_keyboard)
