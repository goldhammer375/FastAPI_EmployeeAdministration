from fastapi import FastAPI

app = FastAPI()

from app.routers import departments, employees, offices
from app.db.db import engine
from sqlmodel import SQLModel


app.include_router(departments.router)
app.include_router(employees.router)
app.include_router(offices.router)

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()