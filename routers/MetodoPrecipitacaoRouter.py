from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.MetodoPrecipitacaoSchemas import MetodoPrecipitacaoSchema, \
    MetodoPrecipitacaoCreateSchema, \
    MetodoPrecipitacaoUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.MetodoPrecipitacaoService import MetodoPrecipitacaoService

metodo_precipitacao_router = APIRouter(
    prefix='/metodo_precipitacao',
    tags=['Metodo Precipitacao']
)


@metodo_precipitacao_router.get('/', response_model=List[MetodoPrecipitacaoSchema],
                                status_code=status.HTTP_200_OK)
async def list_all(
        metodo_precipitacao_service: Annotated[
            MetodoPrecipitacaoService, Depends(MetodoPrecipitacaoService)]):
    return metodo_precipitacao_service.get_all_metodo_precipitacao()


@metodo_precipitacao_router.get('/{metodo_precipitacao_id}', status_code=status.HTTP_200_OK,
                                response_model=MetodoPrecipitacaoSchema,
                                responses={
                                    404: {"description": "Not found",
                                          "model": HTTPExceptionSchemas}})
async def get(metodo_precipitacao_id: int,
              metodo_precipitacao_service: Annotated[
                  MetodoPrecipitacaoService, Depends(MetodoPrecipitacaoService)]):
    return metodo_precipitacao_service.get_metodo_precipitacao_by_id(metodo_precipitacao_id)


@metodo_precipitacao_router.post('/', status_code=status.HTTP_201_CREATED,
                                 response_model=MetodoPrecipitacaoSchema)
async def create(metodo_precipitacao_create: MetodoPrecipitacaoCreateSchema,
                 metodo_precipitacao_service: Annotated[
                     MetodoPrecipitacaoService, Depends(MetodoPrecipitacaoService)]):
    return metodo_precipitacao_service.create_metodo_precipitacao(metodo_precipitacao_create)


@metodo_precipitacao_router.put('/', status_code=status.HTTP_200_OK,
                                response_model=MetodoPrecipitacaoSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(metodo_precipitacao_update: MetodoPrecipitacaoUpdateSchema,
                 metodo_precipitacao_service: Annotated[
                     MetodoPrecipitacaoService, Depends(MetodoPrecipitacaoService)]):
    return metodo_precipitacao_service.update_metodo_precipitacao(metodo_precipitacao_update)


@metodo_precipitacao_router.delete('/{metodo_precipitacao_id}',
                                   status_code=status.HTTP_204_NO_CONTENT,
                                   responses={
                                       404: {"description": "Not found",
                                             "model": HTTPExceptionSchemas}})
async def delete(metodo_precipitacao_id: int,
                 metodo_precipitacao_service: Annotated[
                     MetodoPrecipitacaoService, Depends(MetodoPrecipitacaoService)]):
    return metodo_precipitacao_service.delete_metodo_precipitacao(metodo_precipitacao_id)
