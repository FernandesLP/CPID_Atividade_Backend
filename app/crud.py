from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import func

def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def listar_produtos(db: Session):
    return db.query(models.Produto).all()

def registrar_movimentacao(db: Session, mov: schemas.MovimentacaoCreate):
    db_mov = models.Movimentacao(**mov.dict())
    db.add(db_mov)
    db.commit()
    db.refresh(db_mov)
    return db_mov

def obter_estoque(db: Session, produto_id: int):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if not produto:
        return None

    total_entrada = db.query(func.sum(models.Movimentacao.quantidade)).filter(
        models.Movimentacao.produto_id == produto_id,
        models.Movimentacao.tipo == "entrada"
    ).scalar() or 0

    total_saida = db.query(func.sum(models.Movimentacao.quantidade)).filter(
        models.Movimentacao.produto_id == produto_id,
        models.Movimentacao.tipo == "saida"
    ).scalar() or 0

    return schemas.EstoqueInfo(
        produto_id=produto.id,
        nome=produto.nome,
        total_entrada=total_entrada,
        total_saida=total_saida,
        saldo=total_entrada - total_saida
    )