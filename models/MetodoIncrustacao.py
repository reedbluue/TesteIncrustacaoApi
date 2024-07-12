from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from configs.database import Base


class MetodoIncrustacao(Base):
    __tablename__ = 'METODO_INCRUSTACAO'

    id_metodo_in: Mapped[int] = Column('ID_METODO_IN', Integer, primary_key=True)
    nome: Mapped[str] = Column('NOME', String(300))
    tempo_incrustacao: Mapped[str] = Column('TEMPO_INCRUSTACAO', String(45))
    tempo_reposuso: Mapped[str] = Column('TEMPO_REPOSUSO', String(45))
