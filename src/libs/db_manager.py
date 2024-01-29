import os
import pymongo
from .exception import DBError
from .error_code import DBErrorCode
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


class MongoManager:
    def __init__(
        self, url: str = os.environ.get('MONGO_CONNECTION_URL')
    ) -> None:
        self.url = url
        self.db = os.environ.get('DB_NAME')

    def get_session(self) -> pymongo.MongoClient:
        try:
            self.client = pymongo.MongoClient(self.url)
            return self.client[self.db]
        except Exception as e:
            raise DBError(**DBErrorCode.DBConnectionError.value, err=e)


class PostgreManager:
    def __init__(self) -> None:
        user: str = os.environ.get('USERNAME')
        password: str = os.environ.get('PASSWORD')
        host: str = os.environ.get('POSTGRESQL_HOST')
        db: str = os.environ.get('DB_NAME')
        DATABASE_URL = f'postgresql://{user}:{password}@{host}:5432/{db}'
        self.engine = create_engine(
            DATABASE_URL, pool_size=5, pool_recycle=100, max_overflow=10
        )

    def get_session(self):
        return Session(self.engine)
