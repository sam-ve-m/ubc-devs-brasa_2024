from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: str = Field(..., alias="_id")
    name: str
    email: str
    hashed_password: str
