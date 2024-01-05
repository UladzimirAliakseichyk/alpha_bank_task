from sqlalchemy import create_engine, text
from models.models import Product
from ..models.database import SessionLocal
engine = create_engine('postgresql://dbuser:dbpass@database/dbname')

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
# Добавление данных в базу
for param in params:
    product = Product(title=param['title'], description=param['description'], price=param['price'])
    session.add(product)

# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()
print('items added')
