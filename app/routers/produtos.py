from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/produtos", tags=["Produtos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Produto)
def criar(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, produto)

@router.get("/", response_model=list[schemas.Produto])
def listar(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)

