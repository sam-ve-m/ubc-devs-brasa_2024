from datetime import datetime

from pydantic import BaseModel


class Report(BaseModel):
    user_id: str

    new: bool
    title: str
    content: str
    based_on: str
    created_at: datetime
