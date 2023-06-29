from pydantic import BaseModel


class Payment(BaseModel):
    payment_id: str
    order_id: str
    payment_date: str
    payment_amount: float
    payment_method: str
