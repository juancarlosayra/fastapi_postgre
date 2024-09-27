from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

BASE = declarative_base()

class Task(BASE):
  __tablename__ = 'task'
  id = Column(Integer, primary_key=True, autoincrement=True)
  task_name = Column(String)
  description = Column(String)
  
  def __init__(self, task_name):
    self.task_name = task_name