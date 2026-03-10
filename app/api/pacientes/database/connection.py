from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

DATABASE_URL = "postgresql+asyncpg://arthur:86128931@localhost/doctorhelp"

engine = create_async_engine(DATABASE_URL, echo=True)