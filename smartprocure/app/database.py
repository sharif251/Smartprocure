from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Uses a local SQLite file named procurement.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./procurement.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Helper function to get database session per API request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
