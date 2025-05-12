from app.database.models import async_session
from app.database.models import User, Category, Item, Cart
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()
            
            
async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))
    
    
async def get_category_item(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category == category_id))
    
    
async def add_in_cart(tg_id, item_id: int):
    async with async_session() as session:
        session.add(Cart(tg_id=tg_id, item=item_id))
        await session.commit()


async def get_cart(tg_id):
    async with async_session() as session:
        return await session.scalars(select(Cart).where(Cart.tg_id == tg_id))


async def get_item_name(item_id):
    async with async_session() as session:
        item_name = await session.scalar(select(Item).where(Item.id == item_id))
        return item_name.name
    
    
async def get_item_price(item_id):
    async with async_session() as session:
        item_price = await session.scalar(select(Item).where(Item.id == item_id))
        return item_price.price
    
    

