import uuid
from datetime import datetime
from database.connection import database as db
from models.user import User
from models.log import Log
from services.log_service import create_log
from services.auth_service import hash_password


async def create_user(user: User):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise Exception("Bu e-posta adresi zaten kullanılıyor.")
    user.user_id = str(uuid.uuid4())
    user.password = hash_password(user.password)  # Parolanın hash'lenmesi
    await db.users.insert_one(user.dict())
    await create_log(log=Log(log_id=str(uuid.uuid4()), user_id=user.user_id, action_date=datetime.now(), action_description=f"Kullanıcı oluşturuldu: {user.email}"))


async def get_user(user_id: str):
    user = await db.users.find_one({"user_id": user_id})
    if user:
        return User(**user)
    else:
        raise Exception("Kullanıcı bulunamadı.")


async def update_user(user_id: str, updated_user_data: dict):
    existing_user = await db.users.find_one({"email": updated_user_data.get("email")})
    if existing_user and existing_user["user_id"] != user_id:
        raise Exception("Bu e-posta adresi zaten kullanılıyor.")
    await db.users.update_one({"user_id": user_id}, {"$set": updated_user_data})
    await create_log(log=Log(log_id=str(uuid.uuid4()), user_id=user_id, action_date=datetime.now(), action_description=f"Kullanıcı güncellendi: {user_id}"))


async def delete_user(user_id: str):
    await db.users.delete_one({"user_id": user_id})
    await create_log(log=Log(log_id=str(uuid.uuid4()), user_id=user_id, action_date=datetime.now(), action_description=f"Kullanıcı silindi: {user_id}"))
