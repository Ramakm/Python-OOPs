## Creation of a class 
from random import random
from typing import ItemsView

### We can avoid hard coded variable creattion through instnace of the class by using constructor of the class 
class Item:

    pay_rate = 0.8  ## The pay rate after 20% discount
    def __init__(self, name:str, price:float, quantity: int):   # This method gets created automatically when we create a instance of a class. Its a constructor

        #Run Validation to the received argument
        assert price >= 0, f"Price {price} is not grater than 0"
        assert quantity >=0, f"Quantity {quantity} is not grater than 0"


        # Assign to self Object

        self.name = name   
        self.price = price
        self.quantity = quantity


    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
            
item1 = Item("Phone", 100,5)   # Instance of the clss Item
item1.apply_discount()
print(item1.price)


item2 = Item("Laptop",100,3)   # Instance of the clss Item
item2.apply_discount()
print(item2.price)
# print(item1.pay_rate)
# print(Item.pay_rate)
# print(item2.pay_rate)

print(Item.__dict__) ### All the attributes for class level
print(item1.__dict__)### All the attributes for Instance level




