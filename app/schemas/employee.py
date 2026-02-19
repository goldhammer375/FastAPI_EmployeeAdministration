from pydantic import BaseModel
from app.schemas.department import DepartmentResponse
from app.schemas.office import OfficeResponse

class EmployeeCreate(BaseModel):
    name: str
    position: str
    image_url: str
    department_id: int | None
    office_id: int | None
    boss_id: int | None

class EmployeeUpdate(BaseModel):
    name: str | None
    position: str | None
    image_url: str | None
    department_id: int | None
    office_id: int | None
    boss_id: int | None

class EmployeeShort(BaseModel):
    id: int
    name: str
    position: str
    image_url: str

class EmployeeRead(BaseModel):
    name: str
    position: str
    image_url: str
    department: DepartmentResponse | None
    office: OfficeResponse | None
    boss: EmployeeShort | None

class EmployeeResponse(EmployeeRead):
    id: int
