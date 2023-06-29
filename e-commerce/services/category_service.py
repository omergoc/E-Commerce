import uuid
from datetime import datetime
from database.connection import database as db
from models.category import Category
from models.log import Log
from services.log_service import create_log
from services.auth_service import decode_access_token


async def create_category(category: Category, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    await db.categories.insert_one(category.dict())

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Kategori oluşturuldu: {category.category_id}"))


async def get_category(category_id: str, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    return await db.categories.find_one({"category_id": category_id})


async def update_category(category_id: str, updated_category: Category, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    await db.categories.update_one({"category_id": category_id}, {"$set": updated_category.dict()})

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Kategori güncellendi: {category_id}"))


async def delete_category(category_id: str, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    await db.categories.delete_one({"category_id": category_id})

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Kategori silindi: {category_id}"))
