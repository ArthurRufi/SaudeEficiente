# tratar todas as entradas pessoais de usuarios 

# A troca de dados e confirmação não deve ser feita diretamente por CPF e sim por um ID unico no sistema que vai cruzar os dados com o cpf em outro serviço no backend somente para 
# validação de dados, evitando assim o trafego desnecessário de dados sensíveis.
from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional
from uuid import UUID

class PatientPersonalData(BaseModel):
    id: UUID
    name: str = Field(min_length=2)
    birth_date: date
    address: str = Field(min_length=5)
    phone_number: str = Field(regex=r"^\+?\d{10,15}$")
    email: EmailStr

    principal_parent_name: Optional[str] = None 
    principal_parent_contact: Optional[str] = None

    class Config:
        frozen = True  # 🔒 IMUTÁVEL (value object)
