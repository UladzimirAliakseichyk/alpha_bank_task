from fastapi import FastAPI, Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from models.models import Product
app = FastAPI()

# Пример использования сессии для доступа к базе данных
@app.get("/prods")
async def get_products(skip: int=0, limit: int = 10, db: Session = Depends(SessionLocal)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products