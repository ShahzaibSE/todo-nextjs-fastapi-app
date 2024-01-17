from dotenv import load_dotenv,find_dotenv
import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv, find_dotenv
from database._base_class import Base

_ = load_dotenv(find_dotenv())
# Neon Credientials from .env file.
neon_db_username = os.getenv('PGUSER')
neon_postgresql_password = os.getenv('PGPASSWORD')
neon_connection_url = os.getenv('POSTGRESQL_CONNECTION_URL')

metadata = Base.metadata

connection_string = neon_connection_url
# Database connection string
SQLALCHEMY_DATABASE_URL: str = connection_string if connection_string != None else "<Place your connection string>"
# SQLALCHEMY_DATABASE_URL: str = "postgresql://shahzaibnoor40:eW51bpcoLCxY@ep-restless-glitter-91266254.us-east-2.aws.neon.tech/todoDB?sslmode=require"
# print("Conenction string")
# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

metadata.create_all(engine)

# Creating database session.
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = Session()
        yield db
    finally: 
        db.close()