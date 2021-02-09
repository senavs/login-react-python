from ...settings import database
from .. import DeclarativeBase, engine


class Bootloader:

    def __init__(self, *tables: str, reset: bool = False):
        self.setup(*tables, reset=reset)

    @classmethod
    def setup(cls, *tables: str, reset: bool = False):
        if database.DATABASE_RESET or reset:
            DeclarativeBase.metadata.drop_all(engine)

        if tables:
            table_objects = [DeclarativeBase.metadata.tables[table_name] for table_name in tables]
        else:
            table_objects = None

        DeclarativeBase.metadata.create_all(engine, tables=table_objects)
