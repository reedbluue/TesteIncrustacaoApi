from pydantic import BaseModel, Field

from models.Reagente import Reagente


class ReagenteSchema(BaseModel):
    id_reagente: int
    nome: str
    concentracao: str

    class Config:
        from_attributes = True


class ReagenteCreateSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=300)
    concentracao: str = Field(min_length=1, max_length=10)

    def to_entity(self) -> Reagente:
        return Reagente(**self.dict())


class ReagenteUpdateSchema(ReagenteCreateSchema):
    id_reagente: int
