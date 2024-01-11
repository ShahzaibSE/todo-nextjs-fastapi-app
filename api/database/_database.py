from dotenv import load_dotenv,find_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
connection_string = os.getenv('SQLALCHEMY_DATABASE_URL')
print("Connection String")
print(connection_string)

# Database connection string
SQLALCHEMY_DATABASE_URL: str = connection_string if connection_string != None else "<Place your connection string>"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating database session.
SessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = SessionLoc()
        yield db
    finally: 
        db.close()