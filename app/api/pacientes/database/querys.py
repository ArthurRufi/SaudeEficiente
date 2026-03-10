from uuid import UUID

from pacientes.database.connection import engine
from pacientes.database.query_loader import load_query
from sqlalchemy import text


async def consultarPaciente(id_: UUID):
    async with engine.connect() as conn:
        result = await conn.execute(
            text(load_query("consultar_paciente.sql")),
            {"id_": id_}
        )
        pacientes = result.mappings().first()
        print(pacientes)
        return pacientes