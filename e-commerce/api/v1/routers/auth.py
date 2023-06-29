from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.auth_service import create_access_token, authenticate_user

router = APIRouter()


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    user = await authenticate_user(email, password)
    access_token = create_access_token(user["user_id"])
    return {"access_token": access_token, "token_type": "bearer"}
