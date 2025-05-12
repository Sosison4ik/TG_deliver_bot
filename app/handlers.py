from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.database.requests as rq
import app.keyboards as kb
from config import ADMIN_LIST


router=Router()


@router.message(CommandStart())
async def start(message:Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'Приветствую тебя в нашей доставке еды на дом.Чего желаете?',
                            reply_markup=kb.client_kb)
    

@router.message(F.text == 'Каталог')
async def category(message:Message):
    await message.answer('Выберите категорию продукции:',
                         reply_markup= await kb.category_button())
    print('Что делать?')
    

@router.callback_query(F.data.startswith('category_'))
async def category_item(callback: CallbackQuery):
    category_id = callback.data.split('_')[-1]
    all_item = await rq.get_category_item(category_id)
    await callback.answer(' ')
    for item in all_item:
        await callback.message.answer(f'Название:{item.name}\nОписание:{item.description}\nЦена:{item.price}',
                                reply_markup= await kb.item_button(item.id))
    

@router.callback_query(F.data.startswith('add_to_cart_'))
async def add_to_cart(callback: CallbackQuery):
    await callback.answer('Товар добавлен в корзину')
    item_id = callback.data.split('_')[-1]
    await callback.message.edit_reply_markup(reply_markup = await kb.add_item_button(item_id))
    await rq.add_in_cart(tg_id=callback.from_user.id, item_id=item_id)
    
    
@router.message(F.text == 'Корзина')
async def get_cart(message: Message):
    cart = await rq.get_cart(tg_id = message.from_user.id)
    line = []
    all_price = 0
    if not cart:
        await message.answer('Ваша корзина пуста.')
        
    else:
        for item in cart:
            item_name = await rq.get_item_name(item_id=item.id)
            item_price = await rq.get_item_price(item_id=item.id)
            line.append(f'{item_name} - {item_price} руб.')
            all_price += item_price
        line.append(' ')
        line.append(f'Итого: {all_price} руб.')
        await message.answer(f'{'\n'.join(line)}')
        

    

        
    



