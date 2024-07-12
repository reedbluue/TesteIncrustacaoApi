from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from configs.database import Base


class SolucaoLimpeza(Base):
    __tablename__ = 'SOLUCAO_LIMPEZA'

    id_solucao_limpeza: Mapped[int] = Column('ID_SOLUCAO_LIMPEZA', Integer, primary_key=True)
    nome: Mapped[str] = Column('NOME', String(300))
    concentracao: Mapped[str] = Column('CONCENTRACAO', String(10))
