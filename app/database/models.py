from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import datetime
import enum


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')


async_session = async_sessionmaker(engine)


class OrderState(enum.Enum):
    formalize = 'formalize'
    preparing = 'preparing'
    courier = 'courier'


class Base(AsyncAttrs, DeclarativeBase):
    pass
    

class User(Base):
    __tablename__='users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    
    
class Category(Base):
    __tablename__='categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    
    
class Item(Base):
    __tablename__='items'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(150))
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    
    
class Cart(Base):
    __tablename__ = 'carts'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(ForeignKey('users.id'))
    item = mapped_column(ForeignKey('items.id'))
    
    
# class Order(Base):
#     __tablename__ = 'orders'
    
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     user_phone: Mapped[str] = mapped_column()
#     order_state: Mapped[OrderState] = mapped_column()
    
    





async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)