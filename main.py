from fastapi import FastAPI
from configs.database import Base, engine
from routers.AnaliseMevRouter import analise_mev_router
from routers.FerramentaUsRouter import ferramenta_us_router
from routers.MedidaRouter import medida_router
from routers.MetodoIncrustacaoRouter import metodo_incrustacao_router
from routers.MetodoPrecipitacaoRouter import metodo_precipitacao_router
from routers.ReagenteRouter import reagente_router
from routers.SolucaoIncrustanteRouter import solucao_incrustante_router
from routers.SolucaoLimpezaRouter import solucao_limpeza_router
from routers.TesteRouter import teste_router
from fastapi.middleware.cors import CORSMiddleware
from models import AnaliseMev, FerramentaUs, Medida, MetodoIncrustacao, MetodoPrecipitacao, \
    Reagente, SolucaoIncrustante, SolucaoLimpeza, Teste, SolucaoReagente

Base.metadata.create_all(engine)

app = FastAPI()
origins = ["*",'http://localhost:5173/']



app.include_router(analise_mev_router)
app.include_router(ferramenta_us_router)
app.include_router(metodo_incrustacao_router)
app.include_router(solucao_limpeza_router)
app.include_router(metodo_precipitacao_router)
app.include_router(reagente_router)
app.include_router(solucao_incrustante_router)
app.include_router(teste_router)
app.include_router(medida_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)