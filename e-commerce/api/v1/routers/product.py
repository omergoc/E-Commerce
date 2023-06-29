from fastapi import APIRouter, HTTPException, Depends
from models.product import Product
from services.product_service import create_product, get_product, update_product, delete_product
from services.auth_service import get_current_user

router = APIRouter()


@router.post("/products")
async def create_product_endpoint(product: Product, current_user: dict = Depends(get_current_user)):
    try:
        await create_product(product, current_user['user_id'])
        return {"message": "Ürün başarıyla oluşturuldu."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/products/{product_id}")
async def get_product_endpoint(product_id: str, current_user: dict = Depends(get_current_user)):
    product = await get_product(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Ürün bulunamadı.")


@router.put("/products/{product_id}")
async def update_product_endpoint(product_id: str, updated_product: Product, current_user: dict = Depends(get_current_user)):
    try:
        await update_product(product_id, updated_product, current_user['user_id'])
        return {"message": "Ürün başarıyla güncellendi."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/products/{product_id}")
async def delete_product_endpoint(product_id: str, current_user: dict = Depends(get_current_user)):
    await delete_product(product_id, current_user['user_id'])
    return {"message": "Ürün başarıyla silindi."}
