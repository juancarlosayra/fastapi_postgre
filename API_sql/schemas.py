from typing import Optional
from pydantic import BaseModel, ConfigDict


class Task_Schema(BaseModel):
  id: int
  task_name: str
  description: str
  
  class Config():
    model_config = ConfigDict(from_attributes=True)
  