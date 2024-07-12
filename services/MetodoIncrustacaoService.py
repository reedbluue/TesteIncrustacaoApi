from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.MetodoIncrustacao import MetodoIncrustacao
from schemas.responses.MetodoIncrustacaoSchemas import MetodoIncrustacaoCreateSchema, \
    MetodoIncrustacaoUpdateSchema


class MetodoIncrustacaoService:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.db: Session = session

    def get_all_metodo_incrustacao(self) -> list[Type[MetodoIncrustacao]]:
        return self.db.query(MetodoIncrustacao).all()

    def get_metodo_incrustacao_by_id(self, id_metodo_in: int) -> MetodoIncrustacao:
        metodo_incrustacao = self.db.query(MetodoIncrustacao).filter(
            MetodoIncrustacao.id_metodo_in == id_metodo_in).first()
        if metodo_incrustacao is None:
            raise HTTPException(status_code=404, detail="Metodo Incrustacao not found")
        return metodo_incrustacao

    def create_metodo_incrustacao(self,
                                  metodo_incrustacao_create: MetodoIncrustacaoCreateSchema) -> MetodoIncrustacao:
        entity = metodo_incrustacao_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_metodo_incrustacao(self,
                                  metodo_incrustacao_update: MetodoIncrustacaoUpdateSchema) -> MetodoIncrustacao:
        entity = self.get_metodo_incrustacao_by_id(metodo_incrustacao_update.id_metodo_in)

        entity.nome = metodo_incrustacao_update.nome
        entity.tempo_incrustacao = metodo_incrustacao_update.tempo_incrustacao
        entity.tempo_reposuso = metodo_incrustacao_update.tempo_reposuso

        self.db.commit()
        return entity

    def delete_metodo_incrustacao(self, metodo_incrustacao_id: int) -> None:
        metodo_incrustacao = self.get_metodo_incrustacao_by_id(metodo_incrustacao_id)
        self.db.delete(metodo_incrustacao)
        self.db.commit()
