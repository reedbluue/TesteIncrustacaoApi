import pymssql
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from configs.env import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

engine_init = create_engine(
    f"mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}",
    connect_args={"autocommit": True})

SessionLocalInit = sessionmaker(engine_init)

with SessionLocalInit() as session, session.begin():
    session.execute(text(f"""
    IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{DB_NAME}')
    BEGIN
        CREATE DATABASE {DB_NAME};
    END
    
    """))

engine = create_engine(
    f"mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
