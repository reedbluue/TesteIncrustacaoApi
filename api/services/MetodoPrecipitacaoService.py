from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.MetodoPrecipitacao import MetodoPrecipitacao
from schemas.responses.MetodoPrecipitacaoSchemas import MetodoPrecipitacaoCreateSchema, \
    MetodoPrecipitacaoUpdateSchema


class MetodoPrecipitacaoService:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.db: Session = session

    def get_all_metodo_precipitacao(self) -> list[Type[MetodoPrecipitacao]]:
        return self.db.query(MetodoPrecipitacao).all()

    def get_metodo_precipitacao_by_id(self, id_metodo_pr: int) -> MetodoPrecipitacao:
        metodo_precipitacao = self.db.query(MetodoPrecipitacao).filter(
            MetodoPrecipitacao.id_metodo_pr == id_metodo_pr).first()
        if metodo_precipitacao is None:
            raise HTTPException(status_code=404, detail="Metodo Precipitacao not found")
        return metodo_precipitacao

    def create_metodo_precipitacao(self,
                                   metodo_precipitacao_create: MetodoPrecipitacaoCreateSchema) -> MetodoPrecipitacao:
        entity = metodo_precipitacao_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_metodo_precipitacao(self,
                                   metodo_precipitacao_update: MetodoPrecipitacaoUpdateSchema) -> MetodoPrecipitacao:
        entity = self.get_metodo_precipitacao_by_id(metodo_precipitacao_update.id_metodo_pr)

        entity.nome = metodo_precipitacao_update.nome
        entity.valor = metodo_precipitacao_update.valor

        self.db.commit()
        return entity

    def delete_metodo_precipitacao(self, metodo_precipitacao_id: int) -> None:
        metodo_precipitacao = self.get_metodo_precipitacao_by_id(metodo_precipitacao_id)
        self.db.delete(metodo_precipitacao)
        self.db.commit()
