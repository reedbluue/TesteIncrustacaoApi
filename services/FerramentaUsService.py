from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.FerramentaUs import FerramentaUs
from schemas.responses.FerramentaUsSchemas import FerramentaUsCreateSchema, FerramentaUsUpdateSchema


class FerramentaUsService:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.db: Session = session

    def get_all_ferramenta_us(self) -> list[Type[FerramentaUs]]:
        return self.db.query(FerramentaUs).all()

    def get_ferramenta_us_by_id(self, id_ferramenta: int) -> FerramentaUs:
        ferramenta_us = self.db.query(FerramentaUs).filter(
            FerramentaUs.id_ferramenta == id_ferramenta).first()
        if ferramenta_us is None:
            raise HTTPException(status_code=404, detail="Ferramenta Us not found")
        return ferramenta_us

    def create_ferramenta_us(self, ferramenta_us_create: FerramentaUsCreateSchema) -> FerramentaUs:
        entity = ferramenta_us_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_ferramenta_us(self, ferramenta_us_update: FerramentaUsUpdateSchema) -> FerramentaUs:
        entity = self.get_ferramenta_us_by_id(ferramenta_us_update.id_ferramenta)

        entity.nome = ferramenta_us_update.nome
        entity.frequencia = ferramenta_us_update.frequencia
        entity.potencia = ferramenta_us_update.potencia
        entity.qtd_transdutor = ferramenta_us_update.qtd_transdutor
        entity.impedancia_ferramenta = ferramenta_us_update.impedancia_ferramenta
        entity.impedancia_sistema = ferramenta_us_update.impedancia_sistema

        self.db.commit()
        return entity

    def delete_ferramenta_us(self, ferramenta_us_id: int) -> None:
        ferramenta_us = self.get_ferramenta_us_by_id(ferramenta_us_id)
        self.db.delete(ferramenta_us)
        self.db.commit()
