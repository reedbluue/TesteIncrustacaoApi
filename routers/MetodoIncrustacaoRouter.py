from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.MetodoIncrustacaoSchemas import MetodoIncrustacaoSchema, \
    MetodoIncrustacaoCreateSchema, \
    MetodoIncrustacaoUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.MetodoIncrustacaoService import MetodoIncrustacaoService

metodo_incrustacao_router = APIRouter(
    prefix='/metodo_incrustacao',
    tags=['Metodo Incrustacao']
)


@metodo_incrustacao_router.get('/', response_model=List[MetodoIncrustacaoSchema],
                               status_code=status.HTTP_200_OK)
async def list_all(
        metodo_incrustacao_service: Annotated[
            MetodoIncrustacaoService, Depends(MetodoIncrustacaoService)]):
    return metodo_incrustacao_service.get_all_metodo_incrustacao()


@metodo_incrustacao_router.get('/{metodo_incrustacao_id}', status_code=status.HTTP_200_OK,
                               response_model=MetodoIncrustacaoSchema,
                               responses={
                                   404: {"description": "Not found",
                                         "model": HTTPExceptionSchemas}})
async def get(metodo_incrustacao_id: int,
              metodo_incrustacao_service: Annotated[
                  MetodoIncrustacaoService, Depends(MetodoIncrustacaoService)]):
    return metodo_incrustacao_service.get_metodo_incrustacao_by_id(metodo_incrustacao_id)


@metodo_incrustacao_router.post('/', status_code=status.HTTP_201_CREATED,
                                response_model=MetodoIncrustacaoSchema)
async def create(metodo_incrustacao_create: MetodoIncrustacaoCreateSchema,
                 metodo_incrustacao_service: Annotated[
                     MetodoIncrustacaoService, Depends(MetodoIncrustacaoService)]):
    return metodo_incrustacao_service.create_metodo_incrustacao(metodo_incrustacao_create)


@metodo_incrustacao_router.put('/', status_code=status.HTTP_200_OK,
                               response_model=MetodoIncrustacaoSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(metodo_incrustacao_update: MetodoIncrustacaoUpdateSchema,
                 metodo_incrustacao_service: Annotated[
                     MetodoIncrustacaoService, Depends(MetodoIncrustacaoService)]):
    return metodo_incrustacao_service.update_metodo_incrustacao(metodo_incrustacao_update)


@metodo_incrustacao_router.delete('/{metodo_incrustacao_id}',
                                  status_code=status.HTTP_204_NO_CONTENT,
                                  responses={
                                      404: {"description": "Not found",
                                            "model": HTTPExceptionSchemas}})
async def delete(metodo_incrustacao_id: int,
                 metodo_incrustacao_service: Annotated[
                     MetodoIncrustacaoService, Depends(MetodoIncrustacaoService)]):
    return metodo_incrustacao_service.delete_metodo_incrustacao(metodo_incrustacao_id)
