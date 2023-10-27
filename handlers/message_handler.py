#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from random import randint, choice, shuffle
from datetime import datetime, timedelta
from utils import *
from database import SqlActions
from keyboards import subscription_buy_keyboard, new_word_keyboard, learning_word_keyboard, settings_keyboard


async def subscription_handler(user_data: list, message: types.Message) -> None:
    if user_data[0][2] <= 0:
        text = uk_dict['subscribe_out']
    else:
        expire_date = (datetime.now() + timedelta(days=user_data[0][2])).strftime('%d.%m.%Y')
        text = uk_dict['subscribe'].format(expire_date, user_data[0][2])
    await message.answer(text, reply_markup=subscription_buy_keyboard(user_data[0][1]))


async def new_word_handler(user_data: list, message: types.Message) -> None:
    with SqlActions('words') as sql_words, SqlActions('linkage') as sql_linkage:
        try:
            new_words = sql_words.execute_sql('sql_get_by_level', user_data[0][0])
            if randint(0, 1) == 1 and not new_words:
                word_to_send = sql_words.execute_sql('sql_get_rarest', user_data[0][0])
                sql_linkage.sql_update(cond_column='id', cond_item=word_to_send[0][5], times=int(word_to_send[0][6]) + 1)
                reply_markup = learning_word_keyboard
            else:
                word_to_send = [choice(new_words)]
                reply_markup = new_word_keyboard
            await message.answer(uk_dict['word_translated'].format(str(word_to_send[0][2]).capitalize(),
                                                                   str(word_to_send[0][3]).capitalize()),
                                 reply_markup=reply_markup)
        except:
            await message.answer(uk_dict['words_not_found'])


async def settings_handler(user_data: list, message: types.Message) -> None:
    await message.answer(text=uk_dict['settings'].format(
        user_data[0][3],
        user_data[0][4],
        uk_dict['never'] if user_data[0][5] == 0 else uk_dict['always']
    ), reply_markup=settings_keyboard)


async def test_handler(user_data: list, message: types.Message) -> None:
    with SqlActions('words') as sql_words:
        keyboard = InlineKeyboardBuilder()
        words_list = sql_words.execute_sql('sql_get_words_by_status', user_data[0][0], 0)

        if not words_list:
            words_list = sql_words.execute_sql('sql_get_by_level', user_data[0][0])

        random_word = choice(words_list)
        list_of_words = sql_words.execute_sql('sql_get_random_words', random_word[0])
        list_of_words.append(random_word)
        shuffle(list_of_words)

        is_eng_test = randint(0, 1)
        for words in list_of_words:
            is_test = 'TESTTRUE' if words == random_word else f'TEST{words[0]}'
            keyboard.row(
                types.InlineKeyboardButton(text=str(words[3 if is_eng_test else 2]).capitalize(), callback_data=is_test))

        test_message = uk_dict['test_eng'].format(random_word[2].capitalize()) if is_eng_test \
            else uk_dict['test_ukr'].format(random_word[3].capitalize())

        await message.answer(test_message, reply_markup=keyboard.as_markup())


async def statistics_handler(user_data: list, message: types.Message) -> None:
    with SqlActions('words') as sql_words:
        keyboard = InlineKeyboardBuilder()
        user_id, level = user_data[0][0], user_data[0][3]
        uk_dict_active, uk_dict_learned, uk_dict_details = uk_dict['get_active'], uk_dict['get_learned'], uk_dict['details']

        for status in [1, 0]:
            words = sql_words.execute_sql('sql_get_words_by_status', user_id, status)
            if words:
                text = uk_dict_active if status else uk_dict_learned
                url = create_dictionary(words)
                keyboard.row(types.InlineKeyboardButton(text=text, url=url))

        level_info = sql_words.execute_sql('sql_get_words', user_id, level)[0][0]
        count_words = len(sql_words.sql_query(level=level))

        percentage = round((level_info / count_words) * 100, 2)
        text_details = uk_dict_details.format(level, level_info, count_words, percentage)

        await message.answer(text_details, reply_markup=keyboard.as_markup())


async def get_help_handler(user_data: list, message: types.Message) -> None:
    await message.answer(uk_dict['greeting'])


async def other_words_handler(user_data: list, message: types.Message) -> None:
    with SqlActions('words') as sql_words, SqlActions('linkage') as sql_linkage:
        try:
            keyboard = InlineKeyboardBuilder()
            keyboard.add(types.InlineKeyboardButton(text=uk_dict['get_voice'], callback_data='get_voice'))

            word = sql_words.execute_sql('sql_get_word', message.text, message.text)
            if word:
                is_linked = sql_linkage.execute_sql('sql_get_linkage', str(message.text), str(message.text), user_data[0][0])
                word = word[0]

                if is_linked:
                    if int(is_linked[0][4]) == 1:
                        button_text = uk_dict['have_learned']
                    else:
                        button_text = uk_dict['learn_again']
                else:
                    button_text = uk_dict['learned']

                keyboard.row(types.InlineKeyboardButton(text=button_text, callback_data='have_learned' if button_text == uk_dict['have_learned'] else 'learn_again' if button_text == uk_dict['learn_again'] else 'learned'),
                             types.InlineKeyboardButton(text=uk_dict['not_learned'], callback_data='not_learned'))

                translated_message = uk_dict['word_translated'].format(word[2] if word else translate(message.text)[0], word[3] if word else translate(message.text)[1])
            else:
                keyboard.row(types.InlineKeyboardButton(text=uk_dict['learned'], callback_data='learned'),
                             types.InlineKeyboardButton(text=uk_dict['not_learned'], callback_data='not_learned'))
                translated_result, translated_word = translate(message.text)
                translated_message = uk_dict['word_translated'].format(translated_result, translated_word)

            await message.answer(translated_message, reply_markup=keyboard.as_markup())
        except:
            await message.answer(uk_dict['incorrect'])
