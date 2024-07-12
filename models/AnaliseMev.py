from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from configs.database import Base
from models.Teste import Teste


class AnaliseMev(Base):
    __tablename__ = 'ANALISES_MEV'

    id_analises_mev: Mapped[int] = Column('ID_ANALISES_MEV', Integer, primary_key=True)
    tipo_cristal: Mapped[str] = Column('TIPO_CRISTAL', String(45))
    tamanho_cristal: Mapped[str] = Column('TAMANHO_CRISTAL', String(45))
    magnificacao_mev: Mapped[str] = Column('MAGNIFICACAO_MEV', String(45))
    tensao_mev: Mapped[str] = Column('TENSAO_MEV', String(45))
    wd_mev: Mapped[str] = Column('WD_MEV', String(45))

    id_teste: Mapped[int] = Column('ID_TESTE', Integer, ForeignKey('TESTES.ID_TESTE'))
    teste: Mapped[Teste] = relationship()
