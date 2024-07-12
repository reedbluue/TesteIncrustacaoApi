from typing import List

from pydantic import BaseModel, Field

from models.SolucaoIncrustante import SolucaoIncrustante
from schemas.responses.ReagenteSchemas import ReagenteSchema


class SolucaoIncrustanteSchema(BaseModel):
    nome: str
    id_solucao: int
    tipo_preparo: str
    reagentes: list[ReagenteSchema]

    class Config:
        from_attributes = True


class SolucaoIncrustanteCreateSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=300)
    tipo_preparo: str = Field(min_length=1, max_length=15)

    def to_entity(self) -> SolucaoIncrustante:
        return SolucaoIncrustante(**self.dict())


class SolucaoIncrustanteUpdateSchema(SolucaoIncrustanteCreateSchema):
    id_solucao: int


class SolucaoIncrustanteUpdateReagentesSchema(BaseModel):
    id_solucao: int
    ids_reagentes: List[int]
