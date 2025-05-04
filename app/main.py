from fastapi import FastAPI
from app.routers import produtos, movimentacoes

app = FastAPI()

app.include_router(produtos.router)
app.include_router(movimentacoes.router)