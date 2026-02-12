from medicos.database.connection import engine
from medicos.database.query_loader import load_query
from sqlalchemy import text

query = text(load_query("search_doctors_by_specialty.sql"))


async def get_doctor_by_phone(phone: str):
    async with engine.connect() as conn:
        result = await conn.execute(
            query,
            {"phone": phone}
        )
        doctor = result.mappings().first()
        print(doctor)
        return doctor