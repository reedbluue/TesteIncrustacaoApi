from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.Reagente import Reagente
from schemas.responses.ReagenteSchemas import ReagenteCreateSchema, \
    ReagenteUpdateSchema


class ReagenteService:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.db: Session = session

    def get_all_reagente(self) -> list[Type[Reagente]]:
        return self.db.query(Reagente).all()

    def get_reagente_by_id(self, id_reagente: int) -> Reagente:
        reagente = self.db.query(Reagente).filter(
            Reagente.id_reagente == id_reagente).first()
        if reagente is None:
            raise HTTPException(status_code=404, detail="Reagente not found")
        return reagente

    def get_list_by_ids(self, ids: List[int]) -> List[Reagente]:
        reagentes = list[Reagente]()
        not_found = list[int]()
        for id in ids:
            try:
                reagentes.append(self.get_reagente_by_id(id))
            except HTTPException:
                not_found.append(id)
        if len(not_found) > 0:
            raise HTTPException(status_code=404, detail=f"Reagentes not found: {not_found}")
        return reagentes

    def create_reagente(self,
                        reagente_create: ReagenteCreateSchema) -> Reagente:
        entity = reagente_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_reagente(self,
                        reagente_update: ReagenteUpdateSchema) -> Reagente:
        entity = self.get_reagente_by_id(reagente_update.id_reagente)

        entity.nome = reagente_update.nome
        entity.concentracao = reagente_update.concentracao

        self.db.commit()
        return entity

    def delete_reagente(self, reagente_id: int) -> None:
        reagente = self.get_reagente_by_id(reagente_id)
        self.db.delete(reagente)
        self.db.commit()
