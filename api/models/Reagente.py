from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from configs.database import Base


class Reagente(Base):
    __tablename__ = 'REAGENTES'

    id_reagente: Mapped[int] = Column('ID_REAGENTES', Integer, primary_key=True)
    concentracao: Mapped[str] = Column('CONCENTRACAO', String(10), nullable=True)
    nome: Mapped[str] = Column('NOME', String(300), nullable=True)
