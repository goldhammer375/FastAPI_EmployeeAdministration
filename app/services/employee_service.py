from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from fastapi import Depends, HTTPException
from app.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from app.models.employee import Employee
from app.db.db import get_session


class EmployeeService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self):
        res = self.session.exec(select(Employee).options(
            selectinload(Employee.department),
            selectinload(Employee.office),
            selectinload(Employee.boss)
            )).all()
        return res
    
    def get(self, id: int):
        query = select(Employee).where(Employee.id == id).options(
            selectinload(Employee.department),
            selectinload(Employee.office),
            selectinload(Employee.boss)
        )
        e = self.session.exec(query).first()
        if not e:
            raise HTTPException(status_code = 404,
                                detail = 'Empleado no encontrado')
        return e
    
    def create(self, employee: EmployeeCreate) -> EmployeeResponse:
        e = Employee(**employee.model_dump())
        self.session.add(e)
        self.session.commit()
        self.session.refresh(e, ["department", "office", "boss"])
        return e
    
    def update(self, id: int, employee: EmployeeUpdate) -> Employee:
        e = self.session.get(Employee, id)
        if not e:
            raise HTTPException(status_code = 404,
                                detail = 'Empleado no encontrado')
        
        employee_info = employee.model_dump(exclude_unset=True)
        for key, value in employee_info.items():
            setattr(e, key, value)
        
        self.session.add(e)
        self.session.commit()
        self.session.refresh(e)
        return e
    
    def delete(self, id: int):
        employee = self.session.get(Employee, id)
        if not employee:
            raise HTTPException(status_code = 404,
                                detail = 'Empleado no encontrado')
        self.session.delete(employee)
        self.session.commit()
        return { 'message': 'Empleado eliminado' }