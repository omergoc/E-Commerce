from pydantic import BaseModel


class Product(BaseModel):
    product_id: str
    name: str
    description: str
    price: float
    stock_quantity: int
    category: str
    brand: str
    image_url: str
