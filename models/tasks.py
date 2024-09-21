from sqlalchemy import Column, Integer, String
from config.db import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, default="pending")

