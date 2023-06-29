from database.connection import database
from models.log import Log


async def create_log(log: Log):
    await database.logs.insert_one(log.dict())
