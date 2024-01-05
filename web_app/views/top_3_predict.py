import sys
from models.database import SessionLocal
sys.path.append('../')
from models.models import Product 
import random

def get_top_3():
    session = SessionLocal()

    ids = session.query(Product.id).all()

    all_id_lst = [int(id[0]) for id in ids]

    top_3_prods = random.sample(all_id_lst,3)

    return top_3_prods



if __name__ == '__main__':
    print(get_top_3())
