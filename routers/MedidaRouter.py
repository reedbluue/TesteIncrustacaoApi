from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.MedidaSchemas import MedidaSchema, \
    MedidaCreateSchema, \
    MedidaUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.MedidaService import MedidaService

medida_router = APIRouter(
    prefix='/medida',
    tags=['Medida']
)


@medida_router.get('/', response_model=List[MedidaSchema],
                   status_code=status.HTTP_200_OK)
async def list_all(
        medida_service: Annotated[
            MedidaService, Depends(MedidaService)]):
    return medida_service.get_all_medida()


@medida_router.get('/{medida_id}', status_code=status.HTTP_200_OK,
                   response_model=MedidaSchema,
                   responses={
                       404: {"description": "Not found",
                             "model": HTTPExceptionSchemas}})
async def get(medida_id: int,
              medida_service: Annotated[
                  MedidaService, Depends(MedidaService)]):
    return medida_service.get_medida_by_id(medida_id)


@medida_router.post('/', status_code=status.HTTP_201_CREATED,
                    response_model=MedidaSchema)
async def create(medida_create: MedidaCreateSchema,
                 medida_service: Annotated[
                     MedidaService, Depends(MedidaService)]):
    return medida_service.create_medida(medida_create)


@medida_router.put('/', status_code=status.HTTP_200_OK,
                   response_model=MedidaSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(medida_update: MedidaUpdateSchema,
                 medida_service: Annotated[
                     MedidaService, Depends(MedidaService)]):
    return medida_service.update_medida(medida_update)


@medida_router.delete('/{medida_id}',
                      status_code=status.HTTP_204_NO_CONTENT,
                      responses={
                          404: {"description": "Not found",
                                "model": HTTPExceptionSchemas}})
async def delete(medida_id: int,
                 medida_service: Annotated[
                     MedidaService, Depends(MedidaService)]):
    return medida_service.delete_medida(medida_id)
