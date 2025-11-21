from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from main import DATABASE_URL

DATABASE_URL='sqlite:///./ijarachi.db'

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()