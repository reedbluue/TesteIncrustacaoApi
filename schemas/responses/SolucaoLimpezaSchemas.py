from pydantic import BaseModel, Field

from models.SolucaoLimpeza import SolucaoLimpeza


class SolucaoLimpezaSchema(BaseModel):
    id_solucao_limpeza: int
    nome: str
    concentracao: str

    class Config:
        from_attributes = True


class SolucaoLimpezaCreateSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=300)
    concentracao: str = Field(min_length=1, max_length=10)

    def to_entity(self) -> SolucaoLimpeza:
        return SolucaoLimpeza(**self.dict())


class SolucaoLimpezaUpdateSchema(SolucaoLimpezaCreateSchema):
    id_solucao_limpeza: int
