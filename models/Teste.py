from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from configs.database import Base
from models.FerramentaUs import FerramentaUs
from models.MetodoIncrustacao import MetodoIncrustacao
from models.MetodoPrecipitacao import MetodoPrecipitacao
from models.SolucaoIncrustante import SolucaoIncrustante
from models.SolucaoLimpeza import SolucaoLimpeza


class Teste(Base):
    __tablename__ = 'TESTES'

    id_teste: Mapped[int] = Column('ID_TESTE', Integer, autoincrement=True, primary_key=True)
    operador: Mapped[str] = Column('OPERADOR', String(30))
    regime_escoamento: Mapped[str] = Column('REGIME_ESCOAMENTO', String(15))
    rugosidade: Mapped[str] = Column('RUGOSIDADE', String(15))
    coeficiente: Mapped[str] = Column('COEFICIENTE', String(10))
    metodo_teste: Mapped[str] = Column('METODO_TESTE', String(15))
    ph_solucao: Mapped[str] = Column('PH_SOLUCAO', String(10))
    data_teste: Mapped[datetime] = Column('DATA_TESTE', DateTime)
    metodo_incrustacao_id: Mapped[int] = Column('ID_METODO_IN', Integer,
                                                ForeignKey('METODO_INCRUSTACAO.ID_METODO_IN'),
                                                nullable=False)
    metodo_incrustacao: Mapped[MetodoIncrustacao] = relationship(MetodoIncrustacao)
    solucao_limpeza_id: Mapped[int] = Column('ID_SOLUCAO_LIMPEZA', Integer,
                                             ForeignKey('SOLUCAO_LIMPEZA.ID_SOLUCAO_LIMPEZA'),
                                             nullable=False)
    solucao_limpeza: Mapped[SolucaoLimpeza] = relationship(SolucaoLimpeza)
    metodo_precipitacao_id: Mapped[int] = Column('ID_METODO_PR', Integer,
                                                 ForeignKey('METODO_PRECIPITACAO.ID_METODO_PR'),
                                                 nullable=False)
    metodo_precipitacao: Mapped[MetodoPrecipitacao] = relationship(MetodoPrecipitacao)
    solucao_incrustante_id: Mapped[int] = Column('ID_SOLUCAO', Integer,
                                                 ForeignKey('SOLUCAO_INCRUSTANTE.ID_SOLUCAO'),
                                                 nullable=False)
    solucao_incrustante: Mapped[SolucaoIncrustante] = relationship(SolucaoIncrustante)
    ferramenta_us_id: Mapped[int] = Column('ID_FERRAMENTA_US', Integer,
                                           ForeignKey('FERRAMENTAS_US.ID_FERRAMENTA'),
                                           nullable=False)
    ferramenta_us: Mapped[FerramentaUs] = relationship(FerramentaUs)
