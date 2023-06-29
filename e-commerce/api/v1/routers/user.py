from fastapi import APIRouter, HTTPException, Depends, status
from models.user import User
from services.user_service import create_user, update_user, delete_user,get_user
from services.auth_service import get_current_user
import json
from utilst.helper import object_id_handler


router = APIRouter()


@router.post("/users")
async def create_user_endpoint(user: User):
    try:
        await create_user(user)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}")
async def get_user_endpoint(user_id: str, current_user: dict = Depends(get_current_user)):
    user = await get_user(user_id)
    user_data = json.loads(json.dumps(user.dict(), default=object_id_handler))
    return user_data


@router.put("/users/{user_id}")
async def update_user_endpoint(user_id: str, updated_user: User, current_user: dict = Depends(get_current_user)):
    await update_user(user_id, updated_user.dict())
    return {"message": "User updated successfully"}


@router.delete("/users/{user_id}")
async def delete_user_endpoint(user_id: str, current_user: dict = Depends(get_current_user)):
    if current_user["user_id"] == user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Giriş yapmış kullanıcılar kendi profillerini silemezler")
    await delete_user(user_id)
    return {"message": "User deleted successfully"}


