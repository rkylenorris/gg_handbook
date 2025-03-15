# script for managing a SQLite db for my game's handbook
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from pathlib import Path
import os

db_path = Path("sqlite:///./handbook.db").resolve()

# Create a new SQLite database (or connect to an existing one)
engine = create_engine(db_path)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Define a model for the database   


    
    
    