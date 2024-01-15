from dotenv import load_dotenv,find_dotenv
import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
# Neon Credientials from .env file.
neon_db_username = os.getenv('PGUSER')
neon_postgresql_password = os.getenv('PGPASSWORD')

connection_string = URL.create(
  'postgresql',
  username=neon_db_username,
  password= neon_postgresql_password,
  host='ep-restless-glitter-91266254.us-east-2.aws.neon.tech',
  # host='127.0.0.1',
  # port=8000,
  database='todoDB',
)

# Database connection string
SQLALCHEMY_DATABASE_URL: str = f"{connection_string}?sslmode=require" if connection_string != None else "<Place your connection string>"
# SQLALCHEMY_DATABASE_URL: str = "postgresql://shahzaibnoor40:eW51bpcoLCxY@ep-restless-glitter-91266254.us-east-2.aws.neon.tech/todoDB?sslmode=require" if connection_string != None else "<Place your connection string>"
print("Conenction string")
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating database session.
SessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = SessionLoc()
        yield db
    finally: 
        db.close()