from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item


client_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Информация о заказе')],
    [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню:')


async def category_button():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text = category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text = 'На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def item_button(item_id):
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text = 'Добавить в корзину', callback_data=f'add_to_cart_{item_id}')]
        ]
    )
    return inline_keyboard

async def add_item_button(item_id):
    add_in_cart = InlineKeyboardMarkup(
    inline_keyboard = [[
        InlineKeyboardButton(text='Товар добавлен в корзину✅.Нажмите еще раз для добавления еще порций', callback_data=f'add_to_cart_{item_id}')
    ]]
    )
    return add_in_cart
