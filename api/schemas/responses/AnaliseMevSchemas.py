from pydantic import BaseModel, Field

from models.AnaliseMev import AnaliseMev


class AnaliseMevSchema(BaseModel):
    id_analises_mev: int
    tipo_cristal: str
    tamanho_cristal: str
    magnificacao_mev: str
    tensao_mev: str
    wd_mev: str

    class Config:
        from_attributes = True


class AnaliseMevCreateSchema(BaseModel):
    tipo_cristal: str = Field(min_length=1, max_length=45)
    tamanho_cristal: str = Field(min_length=1, max_length=45)
    magnificacao_mev: str = Field(min_length=1, max_length=45)
    tensao_mev: str = Field(min_length=1, max_length=45)
    wd_mev: str = Field(min_length=1, max_length=45)

    def to_entity(self) -> AnaliseMev:
        return AnaliseMev(**self.dict())


class AnaliseMevUpdateSchema(AnaliseMevCreateSchema):
    id_analises_mev: int