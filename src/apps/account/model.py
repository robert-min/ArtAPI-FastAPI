from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = 'user_account'

    seq = Column(Integer, primary_key=True)
    email = Column(String(500), nullable=False)
    password = Column(LargeBinary, nullable=False)
    name = Column(String(500), nullable=False)
    gender = Column(String(20), nullable=False)
    age = Column(String(200), nullable=False)
    generate_count = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
