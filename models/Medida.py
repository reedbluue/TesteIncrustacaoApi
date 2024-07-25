from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, relationship

from configs.database import Base
from models.Teste import Teste


class Medida(Base):
    __tablename__ = 'MEDIDAS'

    id_medidas: Mapped[int] = Column('ID_MEDIDAS', Integer, autoincrement=True, primary_key=True)
    pressao_incrustacao: Mapped[str] = Column('PRESSAO_INCRUSTACAO', String(45), nullable=True)
    pressao_agua: Mapped[str] = Column('PRESSAO_AGUA', String(45), nullable=True)
    temp_agua_quente_entrada: Mapped[str] = Column('TEMP_AGUA_QUENTE_ENTRADA', String(45), nullable=True)
    temp_agua_quente_saida: Mapped[str] = Column('TEMP_AGUA_QUENTE_SAIDA', String(45), nullable=True)
    temp_agua_fria_entrada: Mapped[str] = Column('TEMP_AGUA_FRIA_ENTRADA', String(45), nullable=True)
    temp_agua_fria_saida: Mapped[str] = Column('TEMP_AGUA_FRIA_SAIDA', String(45), nullable=True)
    delta_t_agua_quente: Mapped[str] = Column('DELTA_T_AGUA_QUENTE', String(45), nullable=True)
    delta_t_agua_fria: Mapped[str] = Column('DELTA_T_AGUA_FRIA', String(45), nullable=True)
    vazao_agua_fria: Mapped[str] = Column('VAZAO_AGUA_FRIA', String(45), nullable=True)
    vazao_agua_quente: Mapped[str] = Column('VAZAO_AGUA_QUENTE', String(45), nullable=True)
    vazao_reagentes: Mapped[str] = Column('VAZAO_REAGENTES', String(45), nullable=True)
    data_coleta: Mapped[datetime] = Column('DATA_COLETA', DateTime)
    id_teste: Mapped[int] = Column('ID_TESTE', Integer, ForeignKey('TESTES.ID_TESTE'))
    teste: Mapped[Teste] = relationship(Teste)
