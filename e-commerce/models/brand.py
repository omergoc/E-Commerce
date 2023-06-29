from pydantic import BaseModel


class Brand(BaseModel):
    brand_id: str
    brand_name: str
