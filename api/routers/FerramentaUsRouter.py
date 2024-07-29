from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.FerramentaUsSchemas import FerramentaUsSchema, FerramentaUsCreateSchema, \
    FerramentaUsUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.FerramentaUsService import FerramentaUsService

ferramenta_us_router = APIRouter(
    prefix='/ferramenta_us',
    tags=['Ferramenta Us']
)


@ferramenta_us_router.get('/', response_model=List[FerramentaUsSchema],
                          status_code=status.HTTP_200_OK)
async def list_all(
        ferramenta_us_service: Annotated[FerramentaUsService, Depends(FerramentaUsService)]):
    return ferramenta_us_service.get_all_ferramenta_us()


@ferramenta_us_router.get('/{ferramenta_us_id}', status_code=status.HTTP_200_OK,
                          response_model=FerramentaUsSchema,
                          responses={
                              404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def get(ferramenta_us_id: int,
              ferramenta_us_service: Annotated[FerramentaUsService, Depends(FerramentaUsService)]):
    return ferramenta_us_service.get_ferramenta_us_by_id(ferramenta_us_id)


@ferramenta_us_router.post('/', status_code=status.HTTP_201_CREATED,
                           response_model=FerramentaUsSchema)
async def create(ferramenta_us_create: FerramentaUsCreateSchema,
                 ferramenta_us_service: Annotated[
                     FerramentaUsService, Depends(FerramentaUsService)]):
    return ferramenta_us_service.create_ferramenta_us(ferramenta_us_create)


@ferramenta_us_router.put('/', status_code=status.HTTP_200_OK,
                          response_model=FerramentaUsSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(ferramenta_us_update: FerramentaUsUpdateSchema,
                 ferramenta_us_service: Annotated[
                     FerramentaUsService, Depends(FerramentaUsService)]):
    return ferramenta_us_service.update_ferramenta_us(ferramenta_us_update)


@ferramenta_us_router.delete('/{ferramenta_us_id}', status_code=status.HTTP_204_NO_CONTENT,
                             responses={
                                 404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def delete(ferramenta_us_id: int,
                 ferramenta_us_service: Annotated[
                     FerramentaUsService, Depends(FerramentaUsService)]):
    return ferramenta_us_service.delete_ferramenta_us(ferramenta_us_id)
