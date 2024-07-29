from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.AnaliseMev import AnaliseMev
from schemas.responses.AnaliseMevSchemas import AnaliseMevCreateSchema, AnaliseMevUpdateSchema


class AnaliseMevService:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.db: Session = session

    def get_all_analise_mev(self) -> list[Type[AnaliseMev]]:
        return self.db.query(AnaliseMev).all()

    def get_analise_mev_by_id(self, id_analises_mev: int) -> AnaliseMev:
        analise_mev = self.db.query(AnaliseMev).filter(
            AnaliseMev.id_analises_mev == id_analises_mev).first()
        if analise_mev is None:
            raise HTTPException(status_code=404, detail="Analise Mev not found")
        return analise_mev

    def create_analise_mev(self, analise_mev_create: AnaliseMevCreateSchema) -> AnaliseMev:
        entity = analise_mev_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_analise_mev(self, analise_mev_update: AnaliseMevUpdateSchema) -> AnaliseMev:
        entity = self.get_analise_mev_by_id(analise_mev_update.id_analises_mev)
        entity.wd_mev = analise_mev_update.wd_mev
        entity.tensao_mev = analise_mev_update.tensao_mev
        entity.magnificacao_mev = analise_mev_update.magnificacao_mev
        entity.tamanho_cristal = analise_mev_update.tamanho_cristal
        entity.tipo_cristal = analise_mev_update.tipo_cristal
        self.db.commit()
        return entity

    def delete_analise_mev(self, analise_mev_id: int) -> None:
        analise_mev = self.get_analise_mev_by_id(analise_mev_id)
        self.db.delete(analise_mev)
        self.db.commit()
