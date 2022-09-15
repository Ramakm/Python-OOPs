## Creation of a class 
from random import random
from typing import ItemsView

class Item:

    pay_rate = 0.8  
    all = []

    def __init__(self, name:str, price:float, quantity: int):   

        assert price >= 0, f"Price {price} is not grater than 0"
        assert quantity >=0, f"Quantity {quantity} is not grater than 0"

        self.name = name   
        self.price = price
        self.quantity = quantity

        # Action to Execute
        Item.all.append(self)

    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price}', '{self.quantity}')"
        
            
item1 = Item("Phone", 100,5)  
item2 = Item("Laptop",100,3)   
item3 = Item("cable",200,6)
item4 = Item("mouse",100,4)
item5 = Item("KeyBoard",300,4)

print(Item.all)
for instance in Item.all:
    print(instance.name)




