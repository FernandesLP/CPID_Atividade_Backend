from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import enum

class TipoMovimentacao(str, enum.Enum):
    entrada = "entrada"
    saida = "saida"

class ProdutoCreate(BaseModel):
    nome: str
    preco: float

class Produto(ProdutoCreate):
    id: int

    class Config:
        orm_mode = True

class MovimentacaoCreate(BaseModel):
    tipo: TipoMovimentacao
    quantidade: int
    produto_id: int

class Movimentacao(MovimentacaoCreate):
    id: int
    data: datetime

    class Config:
        orm_mode = True

class EstoqueInfo(BaseModel):
    produto_id: int
    nome: str
    total_entrada: int
    total_saida: int
    saldo: int