from sqlalchemy.orm import Session
from models.schemes import Item

from models.models import Product


def get_items(db: Session, skip: int = 0, limit: int = 100):
    products = db.query(Product).offset(skip).limit(limit).all()
    items = [
        Item(
            id=product.id,
            title=product.title,
            description=product.description,
            price=product.price,
            )
        for product in products
    ]
    return items