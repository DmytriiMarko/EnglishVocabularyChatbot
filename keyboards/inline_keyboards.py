from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.dict import *

choose_level_keyboard = InlineKeyboardMarkup(inline_keyboard=(
    [[InlineKeyboardButton(text=word, callback_data=callback)] for word, callback in levels][:5]
))

learning_word_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=uk_dict['get_voice'], callback_data='get_voice')],
    [InlineKeyboardButton(text=uk_dict['have_learned'], callback_data='have_learned')]
])

new_word_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=uk_dict['get_voice'], callback_data='get_voice')],
    [InlineKeyboardButton(text=uk_dict['learned'], callback_data='learned'),
     InlineKeyboardButton(text=uk_dict['not_learned'], callback_data='not_learned')]
])

learn_again_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=uk_dict['get_voice'], callback_data='get_voice')],
    [InlineKeyboardButton(text=uk_dict['learned'], callback_data='learned'),
     InlineKeyboardButton(text=uk_dict['not_learned'], callback_data='not_learned')]
])

settings_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=word, callback_data=callback)] for word, callback in settings
])

notification_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=word, callback_data=callback)] for word, callback in notification
])

levels_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=word, callback_data=callback)] for word, callback in levels
])

spoiler_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=word, callback_data=callback)] for word, callback in spoiler
])


def subscription_buy_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=(
            [[InlineKeyboardButton(text=word, url=url.format(user_id))] for word, url in subscription][:3]
        )
    )
