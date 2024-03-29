from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str


class UserUpdate(BaseModel):
    name: str
