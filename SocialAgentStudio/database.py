# database.py
from sqlmodel import create_engine, SQLModel
from models import AgentConfig, PublishedPost

DATABASE_URL = "sqlite:///social_agent.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)