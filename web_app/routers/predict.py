from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from views.load_predict import get_items
from models.schemes import Item
router = APIRouter()

@router.post('/', response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items