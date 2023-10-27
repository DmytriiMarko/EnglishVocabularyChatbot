#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from keyboards import *
from utils import get_voice
from utils import uk_dict
from database import *

settings_reply = {
    "1": {
        "questions": uk_dict['question_1'],
        "reply_markup": levels_keyboard
    },
    "2": {
        "questions": uk_dict['question_2'],
        "reply_markup": notification_keyboard
    },
    "3": {
        "questions": uk_dict['question_3'],
        "reply_markup": spoiler_keyboard
    }
}


async def get_voice_handler(user_data: list, query: types.CallbackQuery) -> None:
    keyboard = InlineKeyboardBuilder()
    old_keyboard = query.message.reply_markup.inline_keyboard
    if len(old_keyboard) > 1 and 'not_learned' in str(old_keyboard):
        keyboard = InlineKeyboardBuilder().row(
            types.InlineKeyboardButton(text=uk_dict['learned'], callback_data='learned'),
            types.InlineKeyboardButton(text=uk_dict['not_learned'], callback_data='not_learned')
        )
    await query.message.edit_reply_markup(reply_markup=keyboard.as_markup())

    file_to_send = get_voice(query.message.text.split('-')[0][2:])
    await query.message.answer_voice(voice=FSInputFile(file_to_send))
    os.remove(file_to_send)


async def select_level_handler(user_data: list, query: types.CallbackQuery) -> None:
    with SqlActions('users') as sql_user:
        level_value = query.data[3:]
        sql_user.sql_update(cond_column="chat_id", cond_item=query.message.chat.id, level=level_value)

        if user_data[0][3]:
            settings_text = uk_dict['settings'].format(
                level_value, user_data[0][4], uk_dict['never'] if user_data[0][5] == 0 else uk_dict['always']
            )
            await query.message.edit_text(text=settings_text, reply_markup=settings_keyboard)
        else:
            await query.message.edit_text(text=uk_dict['question_2'], reply_markup=notification_keyboard)


async def select_notification_handler(user_data: list, query: types.CallbackQuery) -> None:
    with SqlActions('users') as sql_user:
        notification_value = query.data[3:]
        sql_user.sql_update(cond_column="chat_id", cond_item=query.message.chat.id, notification=notification_value)

        if user_data[0][4]:
            settings_text = uk_dict['settings'].format(
                user_data[0][3], notification_value, uk_dict['never'] if user_data[0][5] == 0 else uk_dict['always']
            )
            await query.message.edit_text(text=settings_text, reply_markup=settings_keyboard)
        else:
            await query.message.delete()
            await query.message.answer(text=uk_dict['conclusion'], reply_markup=greeting_keyboard)


async def select_hide_handler(user_data: list, query: types.CallbackQuery) -> None:
    with SqlActions('users') as sql_user:
        sql_user.sql_update(cond_column="chat_id", cond_item=query.message.chat.id, hide=query.data[4:])
        await query.message.edit_text(
            text=uk_dict['settings'].format(
                user_data[0][3],
                user_data[0][3],
                uk_dict['never'] if str(query.data)[4:] == '0' else uk_dict['always']
            ), reply_markup=settings_keyboard)


async def complete_test_handler(user_data: list, query: types.CallbackQuery) -> None:
    with SqlActions('words') as sql_words:
        if query.data.endswith('TRUE'):
            word = sql_words.execute_sql(
                'sql_get_word',
                query.message.text.split(' - ')[0][3:], query.message.text.split(' - ')[0][3:]
            )
            is_linked = sql_words.execute_sql(
                'sql_get_linkage',
                word[0][2], word[0][2], user_data[0][0]
            )

            keyboard = learning_word_keyboard if is_linked and int(is_linked[0][4]) == 1 else learn_again_keyboard if is_linked else new_word_keyboard

            await query.message.edit_text(
                text=uk_dict['word_translated'].format(word[0][2], word[0][3]),
                reply_markup=keyboard
            )
        else:
            old_keyboard = query.message.reply_markup.inline_keyboard
            new_keyboard = []
            for i in old_keyboard:
                if i[0].callback_data == query.data:
                    if uk_dict['wrong'] in i[0].text:
                        return
                    i[0].text += uk_dict['wrong']
                new_keyboard.append(i)

            await query.message.edit_reply_markup(reply_markup=types.InlineKeyboardMarkup(inline_keyboard=new_keyboard))


async def edit_settings_handler(user_data: list, query: types.CallbackQuery) -> None:
    set_info = settings_reply[query.data[3:]]
    await query.message.edit_text(text=set_info["questions"], reply_markup=set_info['reply_markup'], parse_mode='html')


async def word_status_handler(user_data: list, query: types.CallbackQuery) -> None:
    with SqlActions('words') as sql_words, SqlActions('linkage') as sql_linkage:
        words = query.message.text.split(' - ')
        word, translated_word = words[0][3:], words[1][:-3]

        if not sql_words.sql_query(en=word):
            sql_words.sql_insert(level='ALL', en=word, uk=translated_word)

        word_entry = sql_words.sql_query(en=word)
        linkage_entry = sql_linkage.sql_query(user_id=user_data[0][0], word_id=word_entry[0][0])

        keyboard = InlineKeyboardBuilder()
        if len(query.message.reply_markup.inline_keyboard) > 1:
            keyboard.row(types.InlineKeyboardButton(text=uk_dict['get_voice'], callback_data='get_voice'))

        text_suffix = uk_dict.get(query.data, '')
        learned_value = '2' if query.data == 'learned' else '1'

        if not linkage_entry:
            sql_linkage.sql_insert(user_id=user_data[0][0], word_id=word_entry[0][0], learned=learned_value)
        else:
            sql_linkage.sql_update(cond_column='id', cond_item=linkage_entry[0][0], learned=learned_value)

        await query.message.edit_text(text=query.message.text + '\n' + text_suffix, reply_markup=keyboard.as_markup())


async def not_learned_handler(user_data: list, query: types.CallbackQuery) -> None:
    await query.message.edit_text(
        text=query.message.text + uk_dict['have_not_learned'],
        reply_markup=InlineKeyboardBuilder().as_markup()
    )


async def learning_status_handler(user_data: list, query: types.CallbackQuery) -> None:
    with SqlActions('words') as sql_words:
        message_parts = query.message.text.split(' - ')
        word, translated_word = message_parts[0][3:], message_parts[1][:-3]
        word_entry = sql_words.sql_query(en=word)
        times = sql_words.execute_sql('sql_get_times_sent', user_data[0][0], word_entry[0][0])[0][0]
        keyboard = InlineKeyboardBuilder()

        if times < 7 and query.data == 'have_learned':
            keyboard.row(
                types.InlineKeyboardButton(text=uk_dict['yes'], callback_data='have_learned_yes'),
                types.InlineKeyboardButton(text=uk_dict['no'], callback_data='not_learned_no')
            )
            confirmation_text = uk_dict['confirmation'].format(times)
            await query.message.edit_text(text=query.message.text + confirmation_text,
                                          reply_markup=keyboard.as_markup())
        else:
            await query.message.edit_text(text=query.message.text + uk_dict['have_learned_confirmed'],
                                          reply_markup=keyboard.as_markup())
            sql_words.execute_sql('sql_update_linkage', user_data[0][0], word_entry[0][0])
