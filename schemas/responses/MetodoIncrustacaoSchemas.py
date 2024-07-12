from pydantic import BaseModel, Field

from models.MetodoIncrustacao import MetodoIncrustacao


class MetodoIncrustacaoSchema(BaseModel):
    id_metodo_in: int
    nome: str
    tempo_incrustacao: str
    tempo_reposuso: str

    class Config:
        from_attributes = True


class MetodoIncrustacaoCreateSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=300)
    tempo_incrustacao: str = Field(min_length=1, max_length=45)
    tempo_reposuso: str = Field(min_length=1, max_length=45)

    def to_entity(self) -> MetodoIncrustacao:
        return MetodoIncrustacao(**self.dict())


class MetodoIncrustacaoUpdateSchema(MetodoIncrustacaoCreateSchema):
    id_metodo_in: int
