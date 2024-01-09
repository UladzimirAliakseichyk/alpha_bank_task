from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import get_db
from views.load_predict import get_items
from models.schemes import Item
from auth.auth import get_current_user

router = APIRouter()

@router.post('/', response_model=list[Item])
async def predict_items(skip: int = 0, limit: int = 3, 
                        db: Session = Depends(get_db), 
                        user: dict = Depends(get_current_user)):

    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_id = user['id']
    items = get_items(db, skip=skip, limit=limit, user_id=user_id)
    return items
