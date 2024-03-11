from decimal import Decimal
from ecommerce_API.schema.product import Product


products : list[Product] | dict = {
    1: Product(id=1, name="Milk", price=Decimal('250.00'), quantity_available=1),
    2: Product(id=2, name="Sprite", price=Decimal('150.00'), quantity_available=15),
    3: Product(id=3, name="Indomie", price=Decimal('350.50'), quantity_available=5),
}

items = []
for _, product in products.items():
    items.append(product)
    print(items) 