from medicos.database.connection import engine
from medicos.database.query_loader import load_query
from sqlalchemy import text

queryphoneconsult = text(load_query("search_doctors_by_specialty.sql"))
querycrmconsult = text(load_query("search_doctors_by_crm.sql"))
