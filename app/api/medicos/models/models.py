from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class DoctorBase(BaseModel):
    name: str
    specialization: str
    crm: str
    email: EmailStr
    phone: Optional[str] = None

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class Doctor(DoctorBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True