from pydantic import BaseModel, Field

from models.FerramentaUs import FerramentaUs


class FerramentaUsSchema(BaseModel):
    id_ferramenta: int
    nome: str
    frequencia: str
    potencia: str
    qtd_transdutor: str
    impedancia_ferramenta: str
    impedancia_sistema: str

    class Config:
        from_attributes = True


class FerramentaUsCreateSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=300)
    frequencia: str = Field(min_length=1, max_length=45)
    potencia: str = Field(min_length=1, max_length=45)
    qtd_transdutor: str = Field(min_length=1, max_length=45)
    impedancia_ferramenta: str = Field(min_length=1, max_length=45)
    impedancia_sistema: str = Field(min_length=1, max_length=45)

    def to_entity(self) -> FerramentaUs:
        return FerramentaUs(**self.dict())


class FerramentaUsUpdateSchema(FerramentaUsCreateSchema):
    id_ferramenta: int

    def to_entity(self) -> FerramentaUs:
        return FerramentaUs(**self.dict())
