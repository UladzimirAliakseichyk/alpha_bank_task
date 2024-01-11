
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from models.database import SessionLocal
from models.models import Product
from models.models import User
import subprocess
from pathlib import Path


def add_products():
    params = [
        {'title': 'MacBook Pro', 'description': 'Laptop', 'price': 1500},
        {'title': 'Sony PlayStation 5', 'description': 'Gaming Console', 'price': 500},
        {'title': 'Nike Air Max', 'description': 'Sneakers', 'price': 120},
        {'title': 'Canon EOS R5', 'description': 'Camera', 'price': 3500},
        {'title': 'Dyson V11 Vacuum', 'description': 'Vacuum Cleaner', 'price': 600},
        {'title': 'Bose QuietComfort 35 II', 'description': 'Headphones', 'price': 300},
        {'title': 'Amazon Echo Dot', 'description': 'Smart Speaker', 'price': 50},
        {'title': 'Nintendo Switch', 'description': 'Gaming Console', 'price': 300},
        {'title': 'Instant Pot Duo', 'description': 'Pressure Cooker', 'price': 100},
        {'title': 'Fitbit Versa 3', 'description': 'Fitness Tracker', 'price': 230},
        {'title': 'LG OLED TV', 'description': 'Television', 'price': 1500},
        {'title': 'KitchenAid Stand Mixer', 'description': 'Kitchen Appliance', 'price': 300}
    ]

    session = SessionLocal()
    for param in params:
        product = Product(title=param['title'], description=param['description'], price=param['price'])
        session.add(product)

    session.commit()
    session.close()
    print('items added')

def add_test_user():
    session = SessionLocal()

    user_name = 'test_user'
    hashed_password='$2b$12$Q9Mvy3KrjwnoKFvN53msCemgH4CYeZDGhTr985HclS.jVT86KcSxS'

    test_user = User(username=user_name, hashed_password=hashed_password)

    session.add(test_user)

    session.commit()

    session.close()
    print('test_user added')


def read_config_file():
    ini_file_path = Path.cwd()/'prep'/'is_updated.ini'
    print(ini_file_path)
    with open(ini_file_path, 'r') as config_file:
        config_file = config_file.readline()
        print(config_file)
    if 'False' in config_file:
        with open(ini_file_path, 'w') as config_file:
            config_file.write('is_updated = True')
            return False
    return True


def make_migrations():
    try:
        rev_commant = 'alembic revision --autogenerate -m "Initial migration"'
        migration_command = 'alembic upgrade head'
        subprocess.run(rev_commant, shell=True)
        subprocess.run(migration_command, shell=True)
        print('Migrations DONE')
        return True
    except:
        return False
    

def check_db():
    is_db_updated = read_config_file()
    if is_db_updated == False:
        mk_migr = make_migrations()
        if mk_migr == True:
            add_test_user()
            add_products()
        else:
            print('Migrations ERROR')
        

if __name__ == '__main__':
    check_db()