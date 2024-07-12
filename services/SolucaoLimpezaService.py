from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.SolucaoLimpeza import SolucaoLimpeza
from schemas.responses.SolucaoLimpezaSchemas import SolucaoLimpezaCreateSchema, \
    SolucaoLimpezaUpdateSchema


class SolucaoLimpezaService:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.db: Session = session

    def get_all_solucao_limpeza(self) -> list[Type[SolucaoLimpeza]]:
        return self.db.query(SolucaoLimpeza).all()

    def get_solucao_limpeza_by_id(self, id_solucao_limpeza: int) -> SolucaoLimpeza:
        solucao_limpeza = self.db.query(SolucaoLimpeza).filter(
            SolucaoLimpeza.id_solucao_limpeza == id_solucao_limpeza).first()
        if solucao_limpeza is None:
            raise HTTPException(status_code=404, detail="Solucao Limpeza not found")
        return solucao_limpeza

    def create_solucao_limpeza(self,
                               solucao_limpeza_create: SolucaoLimpezaCreateSchema) -> SolucaoLimpeza:
        entity = solucao_limpeza_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_solucao_limpeza(self,
                               solucao_limpeza_update: SolucaoLimpezaUpdateSchema) -> SolucaoLimpeza:
        entity = self.get_solucao_limpeza_by_id(solucao_limpeza_update.id_solucao_limpeza)

        entity.nome = solucao_limpeza_update.nome
        entity.concentracao = solucao_limpeza_update.concentracao

        self.db.commit()
        return entity

    def delete_solucao_limpeza(self, solucao_limpeza_id: int) -> None:
        solucao_limpeza = self.get_solucao_limpeza_by_id(solucao_limpeza_id)
        self.db.delete(solucao_limpeza)
        self.db.commit()
