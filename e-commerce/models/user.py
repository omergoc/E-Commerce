from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    password: str
    address: str
    phone_number: str
    registration_date: str
