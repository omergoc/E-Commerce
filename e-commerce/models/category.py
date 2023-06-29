from pydantic import BaseModel


class Category(BaseModel):
    category_id: str
    category_name: str
    parent_category_id: str
