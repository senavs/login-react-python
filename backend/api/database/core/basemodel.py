from typing import Any, Optional

from .clientconnection import ClientConnection


class BaseModel:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def get(cls, connection: ClientConnection, id: int) -> 'BaseModel':
        return connection.query(cls).get(id)

    def insert(self, connection: ClientConnection, *, commit: bool = True):
        connection.add(self)
        if commit:
            connection.commit()

    def update(self, connection: ClientConnection, *, commit: bool = True, **data: Any):
        for attr, new_value in data.items():
            if new_value is not None:
                setattr(self, attr, new_value)
        if commit:
            connection.commit()

    def delete(self, connection: ClientConnection, *, commit: bool = True):
        connection.session.delete(self)
        if commit:
            connection.commit()

    def to_dict(self, *, exclude: Optional[list] = None, **include) -> dict:
        if not exclude:
            exclude = []

        attrs = {attr.lower(): getattr(self, attr) for attr in self.__dir__() if attr.isupper() and attr not in exclude}
        attrs.update(**include)
        return attrs

    def __repr__(self):
        return f'{type(self).__qualname__}({self.to_dict()})'
