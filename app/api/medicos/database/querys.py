from medicos.database.connection import engine
from medicos.database.query_loader import load_query
from sqlalchemy import text

queryphoneconsult = text(load_query("search_doctors_by_specialty.sql"))
querycrmconsult = text(load_query("search_doctors_by_crm.sql"))

async def get_doctor_by_phone(phone: str):
    async with engine.connect() as conn:
        result = await conn.execute(
            queryphoneconsult,
            {"phone": phone}
        )
        doctor = result.mappings().first()
        print(doctor)
        return doctor
    
async def get_doctor_by_crm(crm_numero: str):
    async with engine.connect() as conn:
        result = await conn.execute(
            querycrmconsult,
            {"crm_numero": crm_numero}
        )
        doctor = result.mappings().first()
        print(doctor)
        return doctor