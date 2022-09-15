## Creation of a class 
from random import random
from typing import ItemsView

### We can avoid hard coded variable creattion through instnace of the class by using constructor of the class 
class Item:

    def __init__(self, name:str, price:float, quantity: int):   # This method gets created automatically when we create a instance of a class. Its a constructor

        #Run Validation to the received argument
        assert price >= 0, f"Price {price} is not grater than 0"
        assert quantity >=0, f"Quantity {quantity} is not grater than 0"


        # Assign to self Object

        self.name = name   ## now we can delete the line item1.name line 
        self.price = price
        self.quantity = quantity


    def calculate_price(self):
        return self.price * self.quantity
            
item1 = Item("Phone", 100,5)   # Instance of the clss Item
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

            
item2 = Item("Laptop",100,3)   # Instance of the clss Item
# item2.name = "Laptop"
# item2.price = 100
# item2.quantity = 3
print(item1.calculate_price())
print(item2.calculate_price())
print(item1.name)
print(item2.name)
print(item1.price)
print(item1.quantity)
print(item2.price)
print(item2.quantity)


