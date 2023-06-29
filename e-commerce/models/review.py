from pydantic import BaseModel


class Review(BaseModel):
    review_id: str
    user_id: str
    product_id: str
    review_text: str
    rating: int
