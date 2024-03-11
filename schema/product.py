from pydantic import BaseModel
from decimal import Decimal

class Product(BaseModel):
    id: int
    name: str
    price: Decimal
    quantity_available: int

class ProductCreate(BaseModel):
    name: str
    price: Decimal
    quantity_available: int

#made changes list[product]
products : list[Product] | dict = {
    1: Product(id=1, name="Milk", price=Decimal('250.00'), quantity_available=1),
    2: Product(id=2, name="Sprite", price=Decimal('150.00'), quantity_available=15),
    3: Product(id=3, name="Indomie", price=Decimal('350.50'), quantity_available=5),
}

# Product,customer and Product 0





         
    
    
  

   

    
      

    


  