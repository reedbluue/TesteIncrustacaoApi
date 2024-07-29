from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.SolucaoIncrustanteSchemas import SolucaoIncrustanteSchema, \
    SolucaoIncrustanteCreateSchema, \
    SolucaoIncrustanteUpdateSchema, SolucaoIncrustanteUpdateReagentesSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.SolucaoIncrustanteService import SolucaoIncrustanteService

solucao_incrustante_router = APIRouter(
    prefix='/solucao_incrustante',
    tags=['Solucao Incrustante']
)


@solucao_incrustante_router.get('/', response_model=List[SolucaoIncrustanteSchema],
                                status_code=status.HTTP_200_OK)
async def list_all(
        solucao_incrustante_service: Annotated[
            SolucaoIncrustanteService, Depends(SolucaoIncrustanteService)]):
    return solucao_incrustante_service.get_all_solucao_incrustante()


@solucao_incrustante_router.get('/{solucao_incrustante_id}', status_code=status.HTTP_200_OK,
                                response_model=SolucaoIncrustanteSchema,
                                responses={
                                    404: {"description": "Not found",
                                          "model": HTTPExceptionSchemas}})
async def get(solucao_incrustante_id: int,
              solucao_incrustante_service: Annotated[
                  SolucaoIncrustanteService, Depends(SolucaoIncrustanteService)]):
    return solucao_incrustante_service.get_solucao_incrustante_by_id(solucao_incrustante_id)


@solucao_incrustante_router.post('/', status_code=status.HTTP_201_CREATED,
                                 response_model=SolucaoIncrustanteSchema)
async def create(solucao_incrustante_create: SolucaoIncrustanteCreateSchema,
                 solucao_incrustante_service: Annotated[
                     SolucaoIncrustanteService, Depends(SolucaoIncrustanteService)]):
    return solucao_incrustante_service.create_solucao_incrustante(solucao_incrustante_create)


@solucao_incrustante_router.put('/', status_code=status.HTTP_200_OK,
                                response_model=SolucaoIncrustanteSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(solucao_incrustante_update: SolucaoIncrustanteUpdateSchema,
                 solucao_incrustante_service: Annotated[
                     SolucaoIncrustanteService, Depends(SolucaoIncrustanteService)]):
    return solucao_incrustante_service.update_solucao_incrustante(solucao_incrustante_update)


@solucao_incrustante_router.put('/reagentes', status_code=status.HTTP_200_OK,
                                response_model=SolucaoIncrustanteSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update_reagentes(update_reagentes: SolucaoIncrustanteUpdateReagentesSchema,
                           solucao_incrustante_service: Annotated[
                               SolucaoIncrustanteService, Depends(SolucaoIncrustanteService)]):
    return solucao_incrustante_service.update_reagentes_solucao_incrustante(update_reagentes)


@solucao_incrustante_router.delete('/{solucao_incrustante_id}',
                                   status_code=status.HTTP_204_NO_CONTENT,
                                   responses={
                                       404: {"description": "Not found",
                                             "model": HTTPExceptionSchemas}})
async def delete(solucao_incrustante_id: int,
                 solucao_incrustante_service: Annotated[
                     SolucaoIncrustanteService, Depends(SolucaoIncrustanteService)]):
    return solucao_incrustante_service.delete_solucao_incrustante(solucao_incrustante_id)
