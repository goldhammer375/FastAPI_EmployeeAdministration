from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentResponse, DepartmentUpdate
from app.db.db import get_session

class DepartmentService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self):
        return self.session.exec(select(Department)).all()
    
    def get(self, id: int):
        query = select(Department).where(Department.id == id)
        d = self.session.exec(query).first()
        if not d:
            raise HTTPException(status_code = 404,
                                detail = 'Departamento no encontrado')
        return d
    
    def create(self, department: DepartmentCreate) -> DepartmentResponse:
        d = Department(**department.model_dump())
        self.session.add(d)
        self.session.commit()
        self.session.refresh(d)
        return d
    
    def update(self, id: int, department: DepartmentUpdate) -> Department:
        d = self.session.get(Department, id)
        if not d:
            raise HTTPException(status_code = 404,
                                detail = 'Departamento no encontrado')
        
        department_info = department.model_dump(exclude_unset=True)
        for key, value in department_info.items():
            setattr(d, key, value)
        
        self.session.add(d)
        self.session.commit()
        self.session.refresh(d)
        return d
    
    def delete(self, id: int):
        department = self.session.get(Department, id)
        if not department:
            raise HTTPException(status_code = 404,
                                detail = 'Departamento no encontrado')
        self.session.delete(department)
        self.session.commit()
        return { 'message': 'Departamento eliminado' }