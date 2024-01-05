from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_neme = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_neme}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

