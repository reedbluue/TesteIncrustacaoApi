from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.TesteSchemas import TesteSchema, \
    TesteCreateSchema, \
    TesteUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.TesteService import TesteService

teste_router = APIRouter(
    prefix='/teste',
    tags=['Teste']
)


@teste_router.get('/', response_model=List[TesteSchema],
                  status_code=status.HTTP_200_OK)
async def list_all(
        teste_service: Annotated[
            TesteService, Depends(TesteService)]):
    return teste_service.get_all_teste()


@teste_router.get('/{teste_id}', status_code=status.HTTP_200_OK,
                  response_model=TesteSchema,
                  responses={
                      404: {"description": "Not found",
                            "model": HTTPExceptionSchemas}})
async def get(teste_id: int,
              teste_service: Annotated[
                  TesteService, Depends(TesteService)]):
    return teste_service.get_teste_by_id(teste_id)


@teste_router.post('/', status_code=status.HTTP_201_CREATED,
                   response_model=TesteSchema)
async def create(teste_create: TesteCreateSchema,
                 teste_service: Annotated[
                     TesteService, Depends(TesteService)]):
    return teste_service.create_teste(teste_create)


@teste_router.put('/', status_code=status.HTTP_200_OK,
                  response_model=TesteSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(teste_update: TesteUpdateSchema,
                 teste_service: Annotated[
                     TesteService, Depends(TesteService)]):
    return teste_service.update_teste(teste_update)


@teste_router.delete('/{teste_id}',
                     status_code=status.HTTP_204_NO_CONTENT,
                     responses={
                         404: {"description": "Not found",
                               "model": HTTPExceptionSchemas}})
async def delete(teste_id: int,
                 teste_service: Annotated[
                     TesteService, Depends(TesteService)]):
    return teste_service.delete_teste(teste_id)
