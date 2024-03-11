from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    username: str
    address: str

class CustomerCreate(BaseModel):
    username: str
    address: str


    
customers: list[Customer] = [
    Customer(id=1, username="martins", address="2, ademola adetokunbo str"),
    Customer(id=2, username="pere", address="23, aminu kano str")
]