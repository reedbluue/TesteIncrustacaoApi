from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.SolucaoLimpezaSchemas import SolucaoLimpezaSchema, \
    SolucaoLimpezaCreateSchema, \
    SolucaoLimpezaUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.SolucaoLimpezaService import SolucaoLimpezaService

solucao_limpeza_router = APIRouter(
    prefix='/solucao_limpeza',
    tags=['Solucao Limpeza']
)


@solucao_limpeza_router.get('/', response_model=List[SolucaoLimpezaSchema],
                            status_code=status.HTTP_200_OK)
async def list_all(
        solucao_limpeza_service: Annotated[
            SolucaoLimpezaService, Depends(SolucaoLimpezaService)]):
    return solucao_limpeza_service.get_all_solucao_limpeza()


@solucao_limpeza_router.get('/{solucao_limpeza_id}', status_code=status.HTTP_200_OK,
                            response_model=SolucaoLimpezaSchema,
                            responses={
                                404: {"description": "Not found",
                                      "model": HTTPExceptionSchemas}})
async def get(solucao_limpeza_id: int,
              solucao_limpeza_service: Annotated[
                  SolucaoLimpezaService, Depends(SolucaoLimpezaService)]):
    return solucao_limpeza_service.get_solucao_limpeza_by_id(solucao_limpeza_id)


@solucao_limpeza_router.post('/', status_code=status.HTTP_201_CREATED,
                             response_model=SolucaoLimpezaSchema)
async def create(solucao_limpeza_create: SolucaoLimpezaCreateSchema,
                 solucao_limpeza_service: Annotated[
                     SolucaoLimpezaService, Depends(SolucaoLimpezaService)]):
    return solucao_limpeza_service.create_solucao_limpeza(solucao_limpeza_create)


@solucao_limpeza_router.put('/', status_code=status.HTTP_200_OK,
                            response_model=SolucaoLimpezaSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(solucao_limpeza_update: SolucaoLimpezaUpdateSchema,
                 solucao_limpeza_service: Annotated[
                     SolucaoLimpezaService, Depends(SolucaoLimpezaService)]):
    return solucao_limpeza_service.update_solucao_limpeza(solucao_limpeza_update)


@solucao_limpeza_router.delete('/{solucao_limpeza_id}',
                               status_code=status.HTTP_204_NO_CONTENT,
                               responses={
                                   404: {"description": "Not found",
                                         "model": HTTPExceptionSchemas}})
async def delete(solucao_limpeza_id: int,
                 solucao_limpeza_service: Annotated[
                     SolucaoLimpezaService, Depends(SolucaoLimpezaService)]):
    return solucao_limpeza_service.delete_solucao_limpeza(solucao_limpeza_id)
