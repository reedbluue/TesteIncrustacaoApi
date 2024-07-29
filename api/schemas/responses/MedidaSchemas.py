from datetime import datetime

from pydantic import BaseModel, Field

from models.Medida import Medida
from schemas.responses.TesteSchemas import TesteSchema


class MedidaSchema(BaseModel):
    id_medidas: int
    pressao_incrustacao: str
    pressao_agua: str
    temp_agua_quente_entrada: str
    temp_agua_quente_saida: str
    temp_agua_fria_entrada: str
    temp_agua_fria_saida: str
    delta_t_agua_quente: str
    delta_t_agua_fria: str
    vazao_agua_fria: str
    vazao_agua_quente: str
    vazao_reagentes: str
    data_coleta: datetime
    id_teste: int | None
    teste: TesteSchema | None

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class MedidaCreateSchema(BaseModel):
    pressao_incrustacao: str = Field(min_length=1, max_length=45)
    pressao_agua: str = Field(min_length=1, max_length=45)
    temp_agua_quente_entrada: str = Field(min_length=1, max_length=45)
    temp_agua_quente_saida: str = Field(min_length=1, max_length=45)
    temp_agua_fria_entrada: str = Field(min_length=1, max_length=45)
    temp_agua_fria_saida: str = Field(min_length=1, max_length=45)
    delta_t_agua_quente: str = Field(min_length=1, max_length=45)
    delta_t_agua_fria: str = Field(min_length=1, max_length=45)
    vazao_agua_fria: str = Field(min_length=1, max_length=45)
    vazao_agua_quente: str = Field(min_length=1, max_length=45)
    vazao_reagentes: str = Field(min_length=1, max_length=45)
    data_coleta: datetime
    id_teste: int | None

    def to_entity(self) -> Medida:
        return Medida(**self.dict())


class MedidaUpdateSchema(MedidaCreateSchema):
    id_medidas: int

    def to_entity(self) -> Medida:
        return Medida(**self.dict())
