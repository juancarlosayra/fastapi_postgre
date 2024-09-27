from fastapi import APIRouter
from sqlalchemy import Select, Insert, Update, Delete
from db import db_session
from models import Task
from schemas import Task_Schema
import json


task = APIRouter()

@task.get("/tasks")
def get_all_tasks():
  tasks = db_session.execute(Select(Task)).fetchall()
  db_session.close()
  task_json = json.dumps(tasks)
  return task_json

@task.get("/tasks/{id}")
def get_task(id: int):
  tasks = db_session.execute(Select(Task).where(Task.id == id))
  db_session.close()
  task_json = json.dumps(tasks)
  return task_json


@task.post("/tasks", response_model=Task_Schema)
def create_task(tasks: Task_Schema):
  new_task = {"id": tasks.id, 
              "task_name": tasks.task_name, 
              "description": tasks.description}
  db_session.execute(Insert(Task).values(new_task))
  
  task_json = json.dumps(new_task)
  
  db_session.commit()
  db_session.close()
  return task_json
  
@task.delete("/tasks/{id}")
def delete_task(id: int):
    db_session.execute(Delete(Task).where(Task.id == id))
    db_session.commit()
    db_session.close()

@task.put("/tasks/{id}")
def update_task(id: int, tasks: Task_Schema):
  updated_task = {"id":tasks.id,
                  "task_name": tasks.task_name, 
                  "description": tasks.description}
  db_session.execute(Update(Task).where(Task.id == id).values(updated_task))
  
  task_json = json.dumps(updated_task)
  
  db_session.commit()
  db_session.close()
  return task_json
  