import sys
from models.database import SessionLocal
sys.path.append('../')
from models.models import Product 
import random
from models.models import User

def check_user_predict(user_id):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()

    if user and user.user_predict: 
        return user.user_predict
    return False




def get_top_3(user_id):

    is_user_has_predict = check_user_predict(user_id)
    
    if is_user_has_predict is False:
        session = SessionLocal()
        user_db = session.query(User).filter(User.id == user_id).first()
        
        ids = session.query(Product.id).all()
        all_id_lst = [int(id[0]) for id in ids]
        if len(all_id_lst) >= 3:
            top_3_prods = random.sample(all_id_lst,3)
            user_db.user_predict = top_3_prods
            session.add(user_db)
            session.commit()
        
            return top_3_prods
        else:
            return None
    values_list = [int(value) for value in is_user_has_predict.strip('{}').split(',')]
    return values_list


if __name__ == '__main__':
    print(get_top_3())
