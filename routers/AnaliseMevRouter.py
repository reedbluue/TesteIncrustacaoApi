from typing import List, Annotated
from fastapi import Depends
from starlette import status
from fastapi import APIRouter

from schemas.responses.AnaliseMevSchemas import AnaliseMevSchema, AnaliseMevCreateSchema, \
    AnaliseMevUpdateSchema
from schemas.exceptions.HTTPExceptionSchemas import HTTPExceptionSchemas
from services.AnaliseMevService import AnaliseMevService

analise_mev_router = APIRouter(
    prefix='/analise_mev',
    tags=['Analise Mev']
)


@analise_mev_router.get('/', response_model=List[AnaliseMevSchema], status_code=status.HTTP_200_OK)
async def list_all(analise_mev_service: Annotated[AnaliseMevService, Depends(AnaliseMevService)]):
    return analise_mev_service.get_all_analise_mev()


@analise_mev_router.get('/{analise_mev_id}', status_code=status.HTTP_200_OK,
                        response_model=AnaliseMevSchema,
                        responses={
                            404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def get(analise_mev_id: int,
              analise_mev_service: Annotated[AnaliseMevService, Depends(AnaliseMevService)]):
    return analise_mev_service.get_analise_mev_by_id(analise_mev_id)


@analise_mev_router.post('/', status_code=status.HTTP_201_CREATED,
                         response_model=AnaliseMevSchema)
async def create(analise_mev_create: AnaliseMevCreateSchema,
                 analise_mev_service: Annotated[AnaliseMevService, Depends(AnaliseMevService)]):
    return analise_mev_service.create_analise_mev(analise_mev_create)


@analise_mev_router.put('/', status_code=status.HTTP_200_OK,
                        response_model=AnaliseMevSchema, responses={
        404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def update(analise_mev_update: AnaliseMevUpdateSchema,
                 analise_mev_service: Annotated[AnaliseMevService, Depends(AnaliseMevService)]):
    return analise_mev_service.update_analise_mev(analise_mev_update)


@analise_mev_router.delete('/{analise_mev_id}', status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {"description": "Not found", "model": HTTPExceptionSchemas}})
async def delete(analise_mev_id: int,
                 analise_mev_service: Annotated[AnaliseMevService, Depends(AnaliseMevService)]):
    return analise_mev_service.delete_analise_mev(analise_mev_id)
