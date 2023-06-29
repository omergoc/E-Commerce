from fastapi import APIRouter, HTTPException
from models.order import Order
from services.order_service import create_order, get_order, update_order, delete_order

router = APIRouter()


@router.post("/orders")
async def create_order_endpoint(order: Order, token: str):
    try:
        await create_order(order, token)
        return {"message": "Sipariş başarıyla oluşturuldu."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/orders/{order_id}")
async def get_order_endpoint(order_id: str, token: str):
    order = await get_order(order_id, token)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Sipariş bulunamadı.")


@router.put("/orders/{order_id}")
async def update_order_endpoint(order_id: str, updated_order: Order, token: str):
    try:
        await update_order(order_id, updated_order, token)
        return {"message": "Sipariş başarıyla güncellendi."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/orders/{order_id}")
async def delete_order_endpoint(order_id: str, token: str):
    await delete_order(order_id, token)
    return {"message": "Sipariş başarıyla silindi."}
