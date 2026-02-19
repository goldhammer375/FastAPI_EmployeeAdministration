from pydantic import BaseModel

class OfficeCreate(BaseModel):
    address: str
    city: str
    country: str
    phone: str

class OfficeUpdate(BaseModel):
    address: str | None
    city: str | None
    country: str | None
    phone: str | None

class OfficeResponse(OfficeCreate):
    id: int