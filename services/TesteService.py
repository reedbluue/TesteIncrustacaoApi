from typing import List, Type, Annotated

from fastapi import HTTPException, Depends

from sqlalchemy.orm import Session

from configs.database import get_db
from models.MetodoPrecipitacao import MetodoPrecipitacao
from models.Teste import Teste
from schemas.responses.TesteSchemas import TesteCreateSchema, TesteUpdateSchema
from services.FerramentaUsService import FerramentaUsService
from services.MetodoIncrustacaoService import MetodoIncrustacaoService
from services.MetodoPrecipitacaoService import MetodoPrecipitacaoService
from services.SolucaoIncrustanteService import SolucaoIncrustanteService
from services.SolucaoLimpezaService import SolucaoLimpezaService


class TesteService:
    def __init__(self, session: Annotated[Session, Depends(get_db)],
                 solucao_incrustante_service: Annotated[
                     SolucaoIncrustanteService, Depends(SolucaoIncrustanteService)],
                 solucao_limpeza_service: Annotated[
                     SolucaoLimpezaService, Depends(SolucaoLimpezaService)],
                 metodo_incrustacao_service: Annotated[
                     MetodoIncrustacaoService, Depends(MetodoIncrustacaoService)],
                 metodo_precipitacao_service: Annotated[
                     MetodoPrecipitacaoService, Depends(MetodoPrecipitacaoService)],
                 ferramentas_us_service: Annotated[
                     FerramentaUsService, Depends(FerramentaUsService)]):
        self.db: Session = session
        self.solucao_incrustante_service = solucao_incrustante_service
        self.solucao_limpeza_service = solucao_limpeza_service
        self.metodo_incrustacao_service = metodo_incrustacao_service
        self.metodo_precipitacao_service = metodo_precipitacao_service
        self.ferramentas_us_service = ferramentas_us_service

    def get_all_teste(self) -> list[Type[Teste]]:
        return self.db.query(Teste).all()

    def get_teste_by_id(self, id_teste: int) -> Teste:
        teste = self.db.query(Teste).filter(
            Teste.id_teste == id_teste).first()
        if teste is None:
            raise HTTPException(status_code=404, detail="Teste not found")
        return teste

    def create_teste(self, teste_create: TesteCreateSchema) -> Teste:
        if teste_create.solucao_incrustante_id is not None:
            self.solucao_incrustante_service.get_solucao_incrustante_by_id(
                teste_create.solucao_incrustante_id)

        if teste_create.solucao_limpeza_id is not None:
            self.solucao_limpeza_service.get_solucao_limpeza_by_id(
                teste_create.solucao_limpeza_id)

        if teste_create.metodo_incrustacao_id is not None:
            self.metodo_incrustacao_service.get_metodo_incrustacao_by_id(
                teste_create.metodo_incrustacao_id)

        if teste_create.metodo_precipitacao_id is not None:
            self.metodo_precipitacao_service.get_metodo_precipitacao_by_id(
                teste_create.metodo_precipitacao_id)

        if teste_create.ferramentas_us_id is not None:
            self.ferramentas_us_service.get_ferramenta_us_by_id(
                teste_create.ferramentas_us_id)

        entity = teste_create.to_entity()
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update_teste(self, teste_update: TesteUpdateSchema) -> Teste:
        entity = self.get_teste_by_id(teste_update.id_teste)

        if teste_update.solucao_incrustante_id is not None:
            self.solucao_incrustante_service.get_solucao_incrustante_by_id(
                teste_update.solucao_incrustante_id)

        if teste_update.solucao_limpeza_id is not None:
            self.solucao_limpeza_service.get_solucao_limpeza_by_id(
                teste_update.solucao_limpeza_id)

        if teste_update.metodo_incrustacao_id is not None:
            self.metodo_incrustacao_service.get_metodo_incrustacao_by_id(
                teste_update.metodo_incrustacao_id)

        if teste_update.metodo_precipitacao_id is not None:
            self.metodo_precipitacao_service.get_metodo_precipitacao_by_id(
                teste_update.metodo_precipitacao_id)

        if teste_update.ferramenta_us_id is not None:
            self.ferramentas_us_service.get_ferramenta_us_by_id(
                teste_update.ferramenta_us_id)

        entity.operador = teste_update.operador
        entity.regime_escoamento = teste_update.regime_escoamento
        entity.rugosidade = teste_update.rugosidade
        entity.coeficiente = teste_update.coeficiente
        entity.metodo_teste = teste_update.metodo_teste
        entity.ph_solucao = teste_update.ph_solucao
        entity.data_teste = teste_update.data_teste

        entity.solucao_incrustante_id = teste_update.solucao_incrustante_id
        entity.solucao_limpeza_id = teste_update.solucao_limpeza_id
        entity.metodo_incrustacao_id = teste_update.metodo_incrustacao_id
        entity.metodo_precipitacao_id = teste_update.metodo_precipitacao_id
        entity.ferramenta_us_id = teste_update.ferramenta_us_id

        self.db.commit()
        return entity

    def delete_teste(self, teste_id: int) -> None:
        teste = self.get_teste_by_id(teste_id)
        self.db.delete(teste)
        self.db.commit()
