# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from models import tasks
from schemas import tasks_schema
from config.db import Base, engine, get_db

def create_table():
  Base.metadata.create_all(bind=engine)
create_table()


app = FastAPI()

@app.get("/")
def get_tasks(db: Session = Depends(get_db)):
  data = db.query(tasks).all()
  
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/tasks", response_model=tasks_schema.TaskBase)
async def create_task(task: tasks_schema.TaskCreate):
    query = tasks.Task.__table__.insert().values(task_name=task.task_name, description=task.description)
    last_record_id = await database.execute(query)
    return {**task.dict(), "id": last_record_id, "status": "pending"}

@app.get("/tasks", response_model=List[tasks_schema.Task])
async def read_tasks(skip: int = 0, limit: int = 10):
    query = tasks.Task.__table__.select().offset(skip).limit(limit)
    return await database.fetch_all(query)

@app.get("/tasks/{task_id}", response_model=tasks_schema.Task)
async def read_task(task_id: int):
    query = tasks.Task.__table__.select().where(tasks.Task.id == task_id)
    task = await database.fetch_one(query)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=tasks_schema.Task)
async def update_task(task_id: int, task: tasks_schema.TaskUpdate):
    query = tasks.Task.__table__.update().where(tasks.Task.id == task_id).values(task_name=task.task_name,
                                                                                 description=task.description,
                                                                                 status=task.status)
    await database.execute(query)
    return {**task.dict(), "id": task_id}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.Task.__table__.delete().where(tasks.Task.id == task_id)
    await database.execute(query)
    return {"detail": "Task deleted"}
