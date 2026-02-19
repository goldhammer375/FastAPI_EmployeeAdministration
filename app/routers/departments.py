from fastapi import APIRouter, Depends
from app.schemas.department import *
from app.services.department_service import DepartmentService

router = APIRouter(prefix = '/departments', tags = ['Departments'])

@router.post('/', response_model = DepartmentResponse)
async def create_department(d: DepartmentCreate, service: DepartmentService = Depends()):
    return service.create(d)

@router.get('/', response_model = list[DepartmentResponse])
async def read_departments(service: DepartmentService = Depends()):
    return service.get_all()

@router.get('/{id}', response_model = DepartmentResponse)
async def read_department(id: int, service: DepartmentService = Depends()):
    return service.get(id)

@router.patch('/{id}', response_model = DepartmentResponse)
async def patch_department(id: int, d: DepartmentUpdate, service: DepartmentService = Depends()):
    return service.update(id, d)

@router.delete('/{id}', response_model = dict[str, str])
async def delete_department(id: int, service: DepartmentService = Depends()):
    return service.delete(id)