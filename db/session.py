from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Replace 'your_database_url' with your actual database URL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/annikmah-management"  # Example URL for SQLite database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()