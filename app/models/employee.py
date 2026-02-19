from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Employee(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    name: str = Field(max_length = 255)
    position: str = Field(max_length = 255)
    image_url: str = Field(max_length = 255)
    department_id: int | None = Field(default = None, foreign_key = 'department.id')
    office_id: int | None = Field(default = None, foreign_key = 'office.id')
    boss_id: int | None = Field(default = None, foreign_key = 'employee.id')


    department: Optional['Department'] = Relationship(back_populates = 'employees')
    office: Optional['Office'] = Relationship(back_populates = 'employees')
    boss: Optional['Employee'] = Relationship(sa_relationship_kwargs = {'remote_side': 'Employee.id'})
    subordinates: list['Employee'] | None = Relationship(back_populates = 'boss') 