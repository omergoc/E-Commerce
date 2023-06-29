from pydantic import BaseModel


class Order(BaseModel):
    order_id: str
    user_id: str
    order_date: str
    total_amount: float
    payment_method: str
    order_status: str
