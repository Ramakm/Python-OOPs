## Creation of a class 
from random import random
from typing import ItemsView


class Item:
    
    def calculate_price(self, x, y):
        return x*y
            
item1 = Item()   # Instance of the clss Item
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity)) 

random_srt = "aaaaavf"
print(random_srt.upper())

print(item1.calculate_price(item1.price, item1.quantity))
