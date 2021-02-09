from pydantic import BaseModel


class User(BaseModel):
    id_user: int
    username: str
