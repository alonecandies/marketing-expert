from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

MYSQL_USER = os.getenv("MYSQL_USER", "marketing_user")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "marketing_pass")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_DB = os.getenv("MYSQL_DB", "marketing_db")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
