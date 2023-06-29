from pydantic import BaseModel
from datetime import datetime


class Log(BaseModel):
    log_id: str
    user_id: str
    action_date: datetime
    action_description: str
