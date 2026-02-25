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
    
async def create_doctor(doctor_data):
    async with engine.connect() as conn:
        result = await conn.execute(
            text(load_query("create_doctor.sql")),
            doctor_data.dict()
        )
        await conn.commit()
        return result.fetchone()
    
def build_update_query(fields: dict) -> str:
    set_clauses = []

    for field in fields.keys():
        set_clauses.append(f"{field} = :{field}")

    set_statement = ", ".join(set_clauses)

    return f"""
        UPDATE doctors
        SET {set_statement},
            update_at = NOW()
        WHERE crm_numero = :crm_numero
        RETURNING *;
    """

async def update_doctor(crm_numero: str, data: dict):

    if not data:
        raise ValueError("No fields to update")

    query = build_update_query(data)

    async with engine.connect() as conn:
        result = await conn.execute(
            text(query),
            {"crm_numero": crm_numero, **data}
        )
        await conn.commit()

        return result.fetchone()