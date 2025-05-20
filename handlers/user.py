from aiogram import F, Router
from aiogram.types import Message
import database

router = Router()

@router.message(F.text == "all")
async def new_test_data(message: Message):
    data = await database.get_all()

    for text in data:
        await message.answer(text.data)

@router.message()
async def new_test_data(message: Message):
    await database.create_test(message.text)


    await message.answer(f"{message.text} added!")
