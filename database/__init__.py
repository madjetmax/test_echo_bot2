from sqlalchemy import delete, select, update, insert

from .engine import session_maker
from .models import TestModel


async def create_test(data):
    async with session_maker() as db_session:
        new_test_data = TestModel(
            data=data
        )
        db_session.add(new_test_data)
        await db_session.commit()

        return new_test_data
        
async def get_all():
    async with session_maker() as db_session:
        query = select(TestModel)
        data = await db_session.execute(query)
        
        return data.scalars().all()