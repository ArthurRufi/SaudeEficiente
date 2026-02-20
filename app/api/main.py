from fastapi import FastAPI
from medicos.domain.doctor.doctorinfos import DoctorInfo, DoctorSpecialty, datetime
from medicos.models.models import Doctor, DoctorCreate, DoctorUpdate
from medicos.database.querys import get_doctor_by_phone, get_doctor_by_crm
app = FastAPI()

@app.get("/")
def main():
    return 

@app.get("/consultardoutor")
def consultar_doutor():

    return {"message": "Consultando doutor..."}

@app.get("/consultardoutorpornome/{phone}")
async def consultar_doutor_por_telefone(phone: str):
    print(f"Consultando doutor com telefone {phone}...")
    doctor = await get_doctor_by_phone(phone)
    return {"message": f"Consultando doutor com telefone {phone}...", "doctor": doctor}

@app.get("/consultarmedicoporcrm/{crm}")
async def consultar_doutor_por_crm(crm: str):
    print(f"Consultando doutor com CRM {crm}...")
    doctor = await get_doctor_by_crm(crm)
    return {"message": f"Consultando doutor com CRM {crm}", "doctor": doctor}

@app.post("/cadastrardoutor")
def cadastrar_doutor(data: DoctorCreate):
    return {"message": f"Cadastrando doutor com nome {data.name}...", "received_data": data}