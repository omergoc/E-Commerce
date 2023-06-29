from pydantic import BaseModel


class Favorite(BaseModel):
    favorite_id: str
    user_id: str
    product_id: str
