from typing import Optional

from sqlalchemy.orm.session import query

from .. import DeclarativeBase, Session


class ClientConnection:
    _session = _query = None

    @property
    def session(self) -> Session:
        return self._session

    @property
    def query(self) -> query:
        return self._query

    def add(self, *obj: DeclarativeBase, commit: Optional[bool] = True):
        self.session.add_all(obj)
        if commit:
            self.commit()

    def delete(self, *obj: DeclarativeBase, commit: Optional[bool] = True):
        for instance in obj:
            self.session.delete(instance)
        if commit:
            self.commit()

    def commit(self):
        self.session.commit()

    def flush(self):
        self.session.flush()

    def rollback(self):
        self.session.rollback()

    def __enter__(self) -> 'ClientConnection':
        self._session = Session()
        self._query = self.session.query
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, Exception):
            self.rollback()
        self.session.close()
