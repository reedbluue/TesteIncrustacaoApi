from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped

from configs.database import Base


class Reagente(Base):
    __tablename__ = 'SOLUCAO_REAGENTE'

    id_solucao: Mapped[int] = Column('ID_SOLUCAO', Integer,
                                     ForeignKey('SOLUCAO_INCRUSTANTE.ID_SOLUCAO'), primary_key=True)
    id_reagente: Mapped[int] = Column('ID_REAGENTE', Integer, ForeignKey('REAGENTES.ID_REAGENTES'),
                                      primary_key=True)
