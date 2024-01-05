from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

sys.path.append('../')
from models.models import Product 

def get_all_id():
    engine = create_engine('postgresql://dbuser:dbpass@database/dbname')
    Session = sessionmaker(bind=engine)
    session = Session()

    ids = session.query(Product.id).all()

    all_id_lst = [int(id[0]) for id in ids]

    return all_id_lst

if __name__ == '__main__':
    get_all_id()
