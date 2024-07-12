from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from configs.database import Base


class MetodoPrecipitacao(Base):
    __tablename__ = 'METODO_PRECIPITACAO'

    id_metodo_pr: Mapped[int] = Column('ID_METODO_PR', Integer, primary_key=True)
    nome: Mapped[str] = Column('NOME', String(300))
    valor: Mapped[str] = Column('VALOR', String(45))