from pydantic import BaseModel

from .user import User


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    user: User


class RegisterRequest(BaseModel):
    username: str
    password: str


class RegisterResponse(BaseModel):
    token: str
    user: User


class ValidateResponse(BaseModel):
    token: str
    user: User
