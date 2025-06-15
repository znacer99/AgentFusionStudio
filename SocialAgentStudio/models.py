# models.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class AgentConfig(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class PublishedPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    platform: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    agent_id: int = Field(foreign_key="agentconfig.id")