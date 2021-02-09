from pydantic import BaseSettings


class APISettings(BaseSettings):
    API_HOST: str = '0.0.0.0'
    API_PORT: int = 8080
    API_DEBUG: bool = False
    API_RELOAD: bool = False
    API_LOG: bool = True


class DatabaseSettings(BaseSettings):
    DATABASE_URI: str = 'mysql://root:toor@mysql:3306/TODO'
    DATABASE_RESET: bool = False


class JWTSettings(BaseSettings):
    SECRET_JEY: str = 'ea5cb8ff0abf6b4ca0080069daaeada0'
    EXPIRED_MINUTES: int = 60


api = APISettings()
database = DatabaseSettings()
jwt = JWTSettings()
