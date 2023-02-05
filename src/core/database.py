import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()

load_dotenv()


def create_session() -> Session:
    db_name = os.getenv("DB_NAME")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASS")
    db_port = os.getenv("DB_PORT")
    db_host = os.getenv("DB_HOST")

    engine = create_engine(
        url=f"postgresql://{username}:{password}@{db_host}:{db_port}/{db_name}"
    )
    
    # Connect and create session
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    return session
