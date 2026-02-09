from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from enum import Enum

class DoctorSpecialty(Enum):
    """Medical specialties"""
    CARDIOLOGY = "Cardiologia"
    NEUROLOGY = "Neurologia"
    PEDIATRICS = "Pediatria"
    ORTHOPEDICS = "Ortopedia"
    PSYCHIATRY = "Psiquiatria"
    GENERAL_PRACTICE = "Clínica Geral"


@dataclass
class DoctorInfo:
    """Doctor information domain model"""
    id: str
    name: str
    crm: str  # Medical registration number
    specialty: DoctorSpecialty
    email: str
    phone: str
    is_active: bool = True
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    def validate(self) -> bool:
        """Validate doctor information"""
        if not self.name or len(self.name) < 3:
            raise ValueError("Name must have at least 3 characters")
        if not self.crm or len(self.crm) < 4:
            raise ValueError("Invalid CRM format")
        if "@" not in self.email:
            raise ValueError("Invalid email format")
        return True

    def deactivate(self) -> None:
        """Deactivate doctor"""
        self.is_active = False
        self.updated_at = datetime.now()

    def activate(self) -> None:
        """Activate doctor"""
        self.is_active = True
        self.updated_at = datetime.now()

    def update_info(self, **kwargs) -> None:
        """Update doctor information"""
        allowed_fields = {"email", "phone", "specialty"}
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
        self.updated_at = datetime.now()