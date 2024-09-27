from fastapi import APIRouter
from sqlalchemy import Select, Insert, Update, Delete
from db import db_session
from models import Task
from schemas import Task_Schema


task = APIRouter()

@task.get("/tasks")
def get_tasks():
  tasks = db_session.execute(Select(Task)).fetchall()
  db_session.close()
  return tasks

@task.post("/tasks", response_model=Task_Schema)
def create_task(tasks: Task_Schema):
  db_session.execute(Insert(Task).values({"id": tasks.id, 
                                          "task_name": tasks.task_name, 
                                          "description": tasks.description}))
  db_session.commit()
  db_session.close()
  
@task.delete("/tasks/{id}")
def delete_task(id: int):
    db_session.execute(Delete(Task).where(Task.id == id))
    db_session.commit()
    db_session.close()

@task.put("/tasks/{id}")
def update_task(id: int, tasks: Task_Schema):
  db_session.execute(Update(Task).where(Task.id == id).values({"task_name": tasks.task_name, 
                                                               "description": tasks.description}))
  db_session.commit()
  db_session.close()
  