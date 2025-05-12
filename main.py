import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router
from app.database.models import async_main




async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit!')
        
    