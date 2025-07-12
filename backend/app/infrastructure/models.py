from sqlalchemy import Column, Integer, String
from .db import Base

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    credits = Column(Integer, default=0)

class CreditModel(Base):
    __tablename__ = "credits"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    description = Column(String(255), default="")
