from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.SolucaoIncrustante import SolucaoIncrustante
from schemas.responses.SolucaoIncrustanteSchemas import SolucaoIncrustanteCreateSchema, \
    SolucaoIncrustanteUpdateSchema, SolucaoIncrustanteUpdateReagentesSchema
from services.ReagenteService import ReagenteService


class SolucaoIncrustanteService:
    def __init__(self, session: Annotated[Session, Depends(get_db)],
                 reagente_service: Annotated[ReagenteService, Depends(ReagenteService)]):
        self.db: Session = session
        self.reagente_service = reagente_service

    def get_all_solucao_incrustante(self) -> list[Type[SolucaoIncrustante]]:
        return self.db.query(SolucaoIncrustante).all()

    def get_solucao_incrustante_by_id(self, id_solucao: int) -> SolucaoIncrustante:
        solucao_incrustante = self.db.query(SolucaoIncrustante).filter(
            SolucaoIncrustante.id_solucao == id_solucao).first()
        if solucao_incrustante is None:
            raise HTTPException(status_code=404, detail="Solucao Incrustante not found")
        return solucao_incrustante

    def create_solucao_incrustante(self,
                                   solucao_incrustante_create: SolucaoIncrustanteCreateSchema) -> SolucaoIncrustante:
        entity = solucao_incrustante_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_solucao_incrustante(self,
                                   solucao_incrustante_update: SolucaoIncrustanteUpdateSchema) -> SolucaoIncrustante:
        entity = self.get_solucao_incrustante_by_id(solucao_incrustante_update.id_solucao)
        entity.nome = solucao_incrustante_update.nome
        entity.tipo_preparo = solucao_incrustante_update.tipo_preparo

        self.db.commit()
        return entity

    def update_reagentes_solucao_incrustante(self,
                                             update_reagentes: SolucaoIncrustanteUpdateReagentesSchema) -> SolucaoIncrustante:
        solucao_incrustante = self.get_solucao_incrustante_by_id(update_reagentes.id_solucao)
        reagentes = self.reagente_service.get_list_by_ids(update_reagentes.ids_reagentes)
        solucao_incrustante.reagentes = reagentes
        self.db.commit()
        self.db.refresh(solucao_incrustante)
        return solucao_incrustante

    def delete_solucao_incrustante(self, solucao_incrustante_id: int) -> None:
        solucao_incrustante = self.get_solucao_incrustante_by_id(solucao_incrustante_id)
        self.db.delete(solucao_incrustante)
        self.db.commit()
