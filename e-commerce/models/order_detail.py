from pydantic import BaseModel


class OrderDetail(BaseModel):
    order_detail_id: str
    order_id: str
    product_id: str
    quantity: int
    unit_price: float
