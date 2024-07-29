from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.ReagenteSchemas import ReagenteSchema, \
    ReagenteCreateSchema, \
    ReagenteUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.ReagenteService import ReagenteService

reagente_router = APIRouter(
    prefix='/reagente',
    tags=['Reagente']
)


@reagente_router.get('/', response_model=List[ReagenteSchema],
                     status_code=status.HTTP_200_OK)
async def list_all(
        reagente_service: Annotated[
            ReagenteService, Depends(ReagenteService)]):
    return reagente_service.get_all_reagente()


@reagente_router.get('/{reagente_id}', status_code=status.HTTP_200_OK,
                     response_model=ReagenteSchema,
                     responses={
                         404: {"description": "Not found",
                               "model": HTTPExceptionSchemas}})
async def get(reagente_id: int,
              reagente_service: Annotated[
                  ReagenteService, Depends(ReagenteService)]):
    return reagente_service.get_reagente_by_id(reagente_id)


@reagente_router.post('/', status_code=status.HTTP_201_CREATED,
                      response_model=ReagenteSchema)
async def create(reagente_create: ReagenteCreateSchema,
                 reagente_service: Annotated[
                     ReagenteService, Depends(ReagenteService)]):
    return reagente_service.create_reagente(reagente_create)


@reagente_router.put('/', status_code=status.HTTP_200_OK,
                     response_model=ReagenteSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(reagente_update: ReagenteUpdateSchema,
                 reagente_service: Annotated[
                     ReagenteService, Depends(ReagenteService)]):
    return reagente_service.update_reagente(reagente_update)


@reagente_router.delete('/{reagente_id}',
                        status_code=status.HTTP_204_NO_CONTENT,
                        responses={
                            404: {"description": "Not found",
                                  "model": HTTPExceptionSchemas}})
async def delete(reagente_id: int,
                 reagente_service: Annotated[
                     ReagenteService, Depends(ReagenteService)]):
    return reagente_service.delete_reagente(reagente_id)
