from fastapi import APIRouter, Depends
from services.category_service import create_category, get_category, update_category, delete_category
from models.category import Category
from services.auth_service import decode_access_token

router = APIRouter()


@router.post("/categories")
async def create_category_endpoint(category: Category, token: str = Depends(decode_access_token)):
    user_id = decode_access_token(token)
    await create_category(category, user_id)
    return {"message": "Kategori oluşturuldu"}


@router.get("/categories/{category_id}")
async def get_category_endpoint(category_id: str, token: str = Depends(decode_access_token)):
    user_id = decode_access_token(token)
    return await get_category(category_id, user_id)


@router.put("/categories/{category_id}")
async def update_category_endpoint(category_id: str, updated_category: Category, token: str = Depends(decode_access_token)):
    user_id = decode_access_token(token)
    await update_category(category_id, updated_category, user_id)
    return {"message": "Kategori güncellendi"}


@router.delete("/categories/{category_id}")
async def delete_category_endpoint(category_id: str, token: str = Depends(decode_access_token)):
    user_id = decode_access_token(token)
    await delete_category(category_id, user_id)
    return {"message": "Kategori silindi"}
