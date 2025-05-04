from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import enum
from datetime import datetime

class TipoMovimentacao(str, enum.Enum):
    entrada = "entrada"
    saida = "saida"

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)

    movimentacoes = relationship("Movimentacao", back_populates="produto")

class Movimentacao(Base):
    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoMovimentacao), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

    produto_id = Column(Integer, ForeignKey("produtos.id"))
    produto = relationship("Produto", back_populates="movimentacoes")