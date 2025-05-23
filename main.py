import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from config import *
import handlers
# from database import engine

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.include_routers(
    handlers.router
)


async def main():

    # db
    # await engine.create_db()

    print('bot launched')
    await dp.start_polling(bot,)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot stoped!")

