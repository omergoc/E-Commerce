import uuid
from datetime import datetime
from database.connection import database as db
from models.order import Order
from models.log import Log
from services.log_service import create_log
from services.auth_service import decode_access_token


async def create_order(order: Order, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    order.user_id = user_id

    await db.orders.insert_one(order.dict())

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Sipariş oluşturuldu: {order.order_id}"))


async def get_order(order_id: str, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    return await db.orders.find_one({"order_id": order_id})


async def update_order(order_id: str, updated_order: Order, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    await db.orders.update_one({"order_id": order_id}, {"$set": updated_order.dict()})

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Sipariş güncellendi: {order_id}"))


async def delete_order(order_id: str, token: str):
    user_id = decode_access_token(token)
    if not user_id:
        raise Exception("Geçersiz token. Kullanıcı girişi yapmanız gerekmektedir.")

    await db.orders.delete_one({"order_id": order_id})

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Sipariş silindi: {order_id}"))
