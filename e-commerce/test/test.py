from datetime import datetime, timedelta
from jose import jwt
from typing import Optional


SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(user_id: str, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user_id, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload["sub"])
        return payload["sub"]
    except jwt.JWTError as e:
        print("Token decode hatası:", str(e))

# Test the functions
user_id = "testuser"
token = create_access_token(user_id)
print("Encoded token:", token)

decoded_user_id = decode_access_token(token)
print("Decoded user id:", decoded_user_id)
