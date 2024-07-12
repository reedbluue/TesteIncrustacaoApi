from pydantic import BaseModel, Field

from models.MetodoPrecipitacao import MetodoPrecipitacao


class MetodoPrecipitacaoSchema(BaseModel):
    id_metodo_pr: int
    nome: str
    valor: str

    class Config:
        from_attributes = True


class MetodoPrecipitacaoCreateSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=300)
    valor: str = Field(min_length=1, max_length=45)

    def to_entity(self) -> MetodoPrecipitacao:
        return MetodoPrecipitacao(**self.dict())


class MetodoPrecipitacaoUpdateSchema(MetodoPrecipitacaoCreateSchema):
    id_metodo_pr: int
