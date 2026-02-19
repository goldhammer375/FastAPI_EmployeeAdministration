from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    name: str

class DepartmentUpdate(BaseModel):
    name: str | None

class DepartmentResponse(DepartmentCreate):
    id: int