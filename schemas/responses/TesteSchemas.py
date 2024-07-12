from datetime import datetime

from pydantic import BaseModel, Field
from models.Teste import Teste
from schemas.responses.FerramentaUsSchemas import FerramentaUsSchema
from schemas.responses.MetodoIncrustacaoSchemas import MetodoIncrustacaoSchema
from schemas.responses.MetodoPrecipitacaoSchemas import MetodoPrecipitacaoSchema
from schemas.responses.SolucaoIncrustanteSchemas import SolucaoIncrustanteSchema
from schemas.responses.SolucaoLimpezaSchemas import SolucaoLimpezaSchema


class TesteSchema(BaseModel):
    id_teste: int
    operador: str
    regime_escoamento: str
    rugosidade: str
    coeficiente: str
    metodo_teste: str
    ph_solucao: str
    data_teste: datetime
    metodo_incrustacao_id: int | None
    metodo_incrustacao: MetodoIncrustacaoSchema | None
    solucao_limpeza_id: int | None
    solucao_limpeza: SolucaoLimpezaSchema | None
    metodo_precipitacao_id: int | None
    metodo_precipitacao: MetodoPrecipitacaoSchema | None
    solucao_incrustante_id: int | None
    solucao_incrustante: SolucaoIncrustanteSchema | None
    ferramenta_us_id: int | None
    ferramenta_us: FerramentaUsSchema | None

    class Config:
        from_attributes = True


class TesteCreateSchema(BaseModel):
    operador: str = Field(min_length=1, max_length=30)
    regime_escoamento: str = Field(min_length=1, max_length=15)
    rugosidade: str = Field(min_length=1, max_length=15)
    coeficiente: str = Field(min_length=1, max_length=10)
    metodo_teste: str = Field(min_length=1, max_length=15)
    ph_solucao: str = Field(min_length=1, max_length=10)
    data_teste: datetime
    metodo_incrustacao_id: int | None
    solucao_limpeza_id: int | None
    metodo_precipitacao_id: int | None
    solucao_incrustante_id: int | None
    ferramenta_us_id: int | None

    def to_entity(self) -> Teste:
        return Teste(**self.dict())


class TesteUpdateSchema(TesteCreateSchema):
    id_teste: int

    def to_entity(self) -> Teste:
        return Teste(**self.dict())
