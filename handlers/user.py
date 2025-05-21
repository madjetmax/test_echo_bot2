from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
import database
from config import *
import datetime
import pytz


router = Router()

def get_expire_date(hours=0, minutes=0, seconds=0) -> datetime.timedelta:
    return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

# test handler
@router.message(Command(commands=["gen"]))
async def genarete_link(message: Message):
    group_id = -1002618313177
    expire_date = get_expire_date(minutes=20)
    
    invite_link = await message.bot.create_chat_invite_link(group_id, expire_date=expire_date, member_limit=1)
    
    await message.answer(invite_link.invite_link)

@router.message(F.text == "all")
async def new_test_data(message: Message):
    data = await database.get_all()
    for text in data:
        await message.answer(f"{text.data}, {text.created}")


@router.message(F.text == "cls")
async def new_test_data(message: Message):
    await database.delete_all()
    await message.answer("deleted all!")


@router.message(F.text)
async def new_test_data(message: Message):
    # await database.create_test(message.text)

    date = datetime.datetime.now(pytz.timezone(MODELS_TIME_ZONE))
    await message.answer(str(date))


