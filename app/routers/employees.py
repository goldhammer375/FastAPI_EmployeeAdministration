from fastapi import APIRouter, Depends
from app.schemas.employee import *
from app.services.employee_service import EmployeeService

router = APIRouter(prefix = '/employees', tags = ['Employees'])

@router.post('/', response_model = EmployeeResponse)
async def create_employee(e: EmployeeCreate, service: EmployeeService = Depends()):
    return service.create(e)

@router.get('/', response_model = list[EmployeeShort])
async def read_employees(service: EmployeeService = Depends()):
    return service.get_all()

@router.get('/{id}', response_model = EmployeeResponse)
async def read_employee(id: int, service: EmployeeService = Depends()):
    return service.get(id)

@router.patch('/{id}', response_model = EmployeeResponse)
async def patch_employee(id: int, e: EmployeeUpdate, service: EmployeeService = Depends()):
    return service.update(id, e)

@router.delete('/{id}', response_model = dict[str, str])
async def delete_employee(id: int, service: EmployeeService = Depends()):
    return service.delete(id)