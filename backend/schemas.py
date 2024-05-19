from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class Message(BaseModel):
    text: str
   # sender_id: int | None
    recipient_id: int

    class Config:            # ORM mode context!
        orm_mode = True
