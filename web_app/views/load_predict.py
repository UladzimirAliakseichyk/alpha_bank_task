from sqlalchemy.orm import Session
from models.schemes import Item
from fastapi import Depends
from sqlalchemy.orm import Session
from models.models import Product
from models.database import get_db


from views.top_3_predict import get_top_3

def get_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    result_top_3 = get_top_3()

    if result_top_3 != None:
        products = db.query(Product).filter(Product.id.in_(result_top_3)).all()
        items = [
            Item(
                id=product.id,
                title=product.title,
                description=product.description,
                price=product.price,
                )
            for product in products
        ]
    
    else:
        items = [
            Item(
                id=0,
                title='None',
                description='None',
                price=0
            )
        ]

    
    return items

