from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID
from ..domain.doctor.doctorinfos import DoctorInfo


class DoctorBase(BaseModel):
    name: str
    specialty: str
    crm: str
    email: EmailStr
    phone: Optional[str] = None

class DoctorCreate(BaseModel):
    name: str
    specialty: str
    crm_numero: str
    crm_uf: str
    email: EmailStr
    phone: str

class DoctorUpdate(BaseModel):
    nome: Optional[str] = None
    specialty: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class Doctor(DoctorBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True