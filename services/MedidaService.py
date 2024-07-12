from typing import Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.Medida import Medida
from schemas.responses.MedidaSchemas import MedidaCreateSchema, MedidaUpdateSchema
from services.TesteService import TesteService


class MedidaService:
    def __init__(self, session: Annotated[Session, Depends(get_db)],
                 teste_service: Annotated[TesteService, Depends(TesteService)]):
        self.db: Session = session
        self.teste_service = teste_service

    def get_all_medida(self) -> list[Type[Medida]]:
        return self.db.query(Medida).all()

    def get_medida_by_id(self, id_medida: int) -> Medida:
        medida = self.db.query(Medida).filter(
            Medida.id_medidas == id_medida).first()
        if medida is None:
            raise HTTPException(status_code=404, detail="Medida not found")
        return medida

    def create_medida(self, medida_create: MedidaCreateSchema) -> Medida:
        if medida_create.id_teste is not None:
            self.teste_service.get_teste_by_id(medida_create.id_teste)

        entity = medida_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_medida(self, medida_update: MedidaUpdateSchema) -> Medida:
        entity = self.get_medida_by_id(medida_update.id_medidas_us)
        if medida_update.id_teste is not None:
            self.teste_service.get_teste_by_id(medida_update.id_teste)

        entity.pressao_incrustacao = medida_update.pressao_incrustacao
        entity.pressao_agua = medida_update.pressao_agua
        entity.temp_agua_quente_entrada = medida_update.temp_agua_quente_entrada
        entity.temp_agua_quente_saida = medida_update.temp_agua_quente_saida
        entity.temp_agua_fria_entrada = medida_update.temp_agua_fria_entrada
        entity.temp_agua_fria_saida = medida_update.temp_agua_fria_saida
        entity.delta_t_agua_quente = medida_update.delta_t_agua_quente
        entity.delta_t_agua_fria = medida_update.delta_t_agua_fria
        entity.vazao_agua_fria = medida_update.vazao_agua_fria
        entity.vazao_agua_quente = medida_update.vazao_agua_quente
        entity.vazao_reagentes = medida_update.vazao_reagentes
        entity.data_coleta = medida_update.data_coleta

        entity.teste_id = medida_update.id_teste

        self.db.commit()
        return entity

    def delete_medida(self, medida_id: int) -> None:
        medida = self.get_medida_by_id(medida_id)
        self.db.delete(medida)
        self.db.commit()
