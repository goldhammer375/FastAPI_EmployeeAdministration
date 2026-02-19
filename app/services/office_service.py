from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from fastapi import Depends, HTTPException
from app.models.office import Office
from app.schemas.office import OfficeCreate, OfficeResponse, OfficeUpdate
from app.db.db import get_session

class OfficeService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self):
        return self.session.exec(select(Office)).all()
    
    def get(self, id: int):
        query = select(Office).where(Office.id == id)
        o = self.session.exec(query).first()
        if not o:
            raise HTTPException(status_code = 404,
                                detail = 'Oficina no encontrada')
        return o
        
    def create(self, office: OfficeCreate) -> OfficeResponse:
        o = Office(**office.model_dump())
        self.session.add(o)
        self.session.commit()
        self.session.refresh(o)
        return o

    def update(self, id: int, office: OfficeUpdate) -> Office:
        o = self.session.get(Office, id)
        if not o:
            raise HTTPException(status_code = 404,
                                detail = 'Oficina no encontrada')
        
        office_info = office.model_dump(exclude_unset=True)
        for key, value in office_info.items():
            setattr(o, key, value)
        
        self.session.add(o)
        self.session.commit()
        self.session.refresh(o)
        return o
    
    def delete(self, id: int):
        office = self.session.get(Office, id)
        if not office:
            raise HTTPException(status_code = 404,
                                detail = 'Oficina no encontrada')
        self.session.delete(office)
        self.session.commit()
        return { 'message': 'Oficina eliminada' }