from pydantic import BaseModel


class DiscountCoupon(BaseModel):
    discount_id: str
    discount_name: str
    discount_code: str
    discount_rate: float
    start_date: str
    end_date: str
