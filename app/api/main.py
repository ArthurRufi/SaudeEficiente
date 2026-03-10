from fastapi import FastAPI, HTTPException
from medicos.domain.doctor.doctorinfos import DoctorInfo, DoctorSpecialty, datetime
from medicos.models.models import Doctor, DoctorCreate, DoctorUpdate
from medicos.database.querys import get_doctor_by_phone, get_doctor_by_crm, create_doctor, update_doctor
from pacientes.database.querys import consultarPaciente
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
async def cadastrar_doutor(data: DoctorCreate):
    doctor = await create_doctor(data)
    return {"message": f"Cadastrando doutor com nome {data.name}...", "received_data": data}


@app.put("/atualizardoutor/{crm_numero}")
async def atualizar_doutor(crm_numero: str, data: DoctorUpdate):

    update_data = data.dict(exclude_unset=True)

    print("Dados recebidos:", update_data)  # DEBUG

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Envie pelo menos um campo para atualizar"
        )

    updated_doctor = await update_doctor(crm_numero=crm_numero, data=update_data)

    if not updated_doctor:
        raise HTTPException(status_code=404, detail="Doutor não encontrado")

    return {
        "message": "Doutor atualizado com sucesso",
        "doctor": dict(updated_doctor._mapping)
    }

# PACIENTES
# _______________________________________________________________________#
@app.get("/consultarpaciente/{id}")
async def search_pacientes(id: str):
    print(f"Consultando paciente por id {id}")
    paciente =  await consultarPaciente(id)
    return {"message": f"Consultando a mizera do paciente {id}", "pacitene" : paciente} 
