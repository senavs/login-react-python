from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database.core import Bootloader
from .modules.errorhandler import ErrorHandler
from .routes import router

__version__ = '1.0.1'

app = FastAPI(title='Login API',
              description='Login project application with Python, React and JWT.',
              version=__version__)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

ErrorHandler(app)
Bootloader()
