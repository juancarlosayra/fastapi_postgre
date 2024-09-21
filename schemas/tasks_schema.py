from pydantic import BaseModel

class TaskBase(BaseModel):
    task_name: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    status: str

class Task(TaskBase):
    id: int
    status: str

    class Config:
        orm_mode = True