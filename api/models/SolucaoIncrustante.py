from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from configs.database import Base
from models.Reagente import Reagente


class SolucaoIncrustante(Base):
    __tablename__ = 'SOLUCAO_INCRUSTANTE'

    id_solucao: Mapped[int] = Column('ID_SOLUCAO', Integer, primary_key=True)
    tipo_preparo: Mapped[str] = Column('TIPO_PREPARO', String(15), nullable=True)
    nome: Mapped[str] = Column('NOME', String(300), nullable=True)

    reagentes: Mapped[list[Reagente]] = relationship(secondary="SOLUCAO_REAGENTE")
