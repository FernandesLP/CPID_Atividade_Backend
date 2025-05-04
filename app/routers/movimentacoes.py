from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/movimentacoes", tags=["Movimentacoes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Movimentacao)
def movimentar(mov: schemas.MovimentacaoCreate, db: Session = Depends(get_db)):
    return crud.registrar_movimentacao(db, mov)

@router.get("/estoque/{produto_id}", response_model=schemas.EstoqueInfo)
def estoque(produto_id: int, db: Session = Depends(get_db)):
    estoque = crud.obter_estoque(db, produto_id)
    if estoque is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return estoque