import uuid
from datetime import datetime
from database.connection import database as db
from models.product import Product
from services.log_service import create_log
from models.log import Log


async def create_product(product: Product, user_id: str):
    existing_product = await db.products.find_one({"product_id": product.product_id})
    if existing_product:
        raise Exception("Bu ürün zaten var.")

    await db.products.insert_one(product.dict())

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Ürün oluşturuldu: {product.product_id}"))


async def get_product(product_id: str):
    return await db.products.find_one({"product_id": product_id})


async def update_product(product_id: str, updated_product: Product, user_id: str):
    existing_product = await db.products.find_one({"product_id": product_id})
    if not existing_product:
        raise Exception("Ürün bulunamadı.")

    await db.products.update_one({"product_id": product_id}, {"$set": updated_product.dict()})

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Ürün güncellendi: {product_id}"))


async def delete_product(product_id: str, user_id: str):
    existing_product = await db.products.find_one({"product_id": product_id})
    if not existing_product:
        raise Exception("Ürün bulunamadı.")

    await db.products.delete_one({"product_id": product_id})

    await create_log(log=Log(log_id=uuid.uuid4().hex, user_id=user_id, action_date=datetime.now(),
                             action_description=f"Ürün silindi: {product_id}"))
