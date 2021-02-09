from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..settings import database

engine = create_engine(database.DATABASE_URI, echo=False)
DeclarativeBase = declarative_base()
Session = sessionmaker(engine)

from .core import *  # noqa
from .models import *  # noqa
