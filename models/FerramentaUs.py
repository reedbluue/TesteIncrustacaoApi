from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from configs.database import Base


class FerramentaUs(Base):
    __tablename__ = 'FERRAMENTAS_US'

    id_ferramenta: Mapped[int] = Column('ID_FERRAMENTA', Integer, primary_key=True)
    nome: Mapped[str] = Column('NOME', String(300))
    frequencia: Mapped[str] = Column('FREQUENCIA', String(45))
    potencia: Mapped[str] = Column('POTENCIA', String(45))
    qtd_transdutor: Mapped[str] = Column('QTD_TRANSDUTOR', String(45))
    impedancia_ferramenta: Mapped[str] = Column('IMPEDANCIA_FERRAMENTA', String(45))
    impedancia_sistema: Mapped[str] = Column('IMPEDANCIA_SISTEMA', String(45))
