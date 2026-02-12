from fastapi import FastAPI
from medicos.domain.doctor.doctorinfos import DoctorInfo, DoctorSpecialty, datetime
from medicos.models.models import Doctor, DoctorCreate, DoctorUpdate
from medicos.database.querys import get_doctor_by_phone
app = FastAPI()

@app.get("/")
def main():
    return 

@app.get("/consultardoutor")
def consultar_doutor():

    return {"message": "Consultando doutor..."}

@app.get("/consultardoutorpornm/{phone}")
async def consultar_doutor_por_telefone(phone: str):
    print(f"Consultando doutor com telefone {phone}...")
    doctor = await get_doctor_by_phone(phone)
    return {"message": f"Consultando doutor com telefone {phone}...", "doctor": doctor}