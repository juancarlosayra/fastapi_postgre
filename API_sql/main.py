from fastapi import FastAPI
from task_routes import task

app = FastAPI()

@app.get("/")
def helloworld():
  return "Hello World"


app.include_router(task)
