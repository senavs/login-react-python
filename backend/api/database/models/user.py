import re

from bcrypt import checkpw, gensalt, hashpw
from fastapi import HTTPException
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.sql import func

from .. import BaseModel, DeclarativeBase


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'USER'

    ID_USER = Column(Integer, autoincrement=True, nullable=False, primary_key=True, unique=True)
    USERNAME = Column(String(32), nullable=False, unique=False)
    PASSWORD = Column(String(72), nullable=False, unique=False)
    CREATED_AT = Column(DateTime, nullable=False, unique=False, default=func.now(), server_default=func.now())
    UPDATED_AT = Column(DateTime, nullable=False, unique=False, default=func.now(), server_default=func.now(), onupdate=func.now(), server_onupdate=func.now())

    def __init__(self, PASSWORD: str, **kwargs):
        super().__init__(**kwargs)
        self.PASSWORD = self.generate_password(PASSWORD)

    @validates('USERNAME')
    def validate_name(self, key, value):
        is_valid, edited_username = self.check_username(value)
        if not is_valid:
            raise HTTPException(404, f'invalid username. try: {edited_username}')
        return value

    @classmethod
    def check_username(cls, username: str) -> tuple[bool, str]:
        username_regex = r'[^a-zA-Z0-9._\s]'
        new_username = re.sub(username_regex, '', username.strip())
        is_valid = False if re.findall(username_regex, username) else True

        return is_valid, new_username

    @classmethod
    def generate_password(cls, password: str):
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return checkpw(password.encode('utf-8'), self.PASSWORD.encode('utf-8'))
