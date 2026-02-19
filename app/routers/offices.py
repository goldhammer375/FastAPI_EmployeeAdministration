from fastapi import APIRouter, Depends
from app.schemas.office import *
from app.services.office_service import OfficeService

router = APIRouter(prefix = '/offices', tags = ['Offices'])

@router.post('/', response_model = OfficeResponse)
async def create_office(o: OfficeCreate, service: OfficeService = Depends()):
    return service.create(o)

@router.get('/', response_model = list[OfficeResponse])
async def read_offices(service: OfficeService = Depends()):
    return service.get_all()

@router.get('/{id}', response_model = OfficeResponse)
async def read_office(id: int, service: OfficeService = Depends()):
    return service.get(id)

@router.patch('/{id}', response_model = OfficeResponse)
async def patch_office(id: int, o: OfficeUpdate, service: OfficeService = Depends()):
    return service.update(id, o)

@router.delete('/{id}', response_model = dict[str, str])
async def delete_office(id: int, service: OfficeService = Depends()):
    return service.delete(id)