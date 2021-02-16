# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:03:56 2021

@author: dhtmd
"""

products = {"냉장고":220,"건조기":140,"TV":130,"세탁기":150,"오디오":50,"컴퓨터":250}
print(products)
product1 = {}
product1set = []
for name in products.keys():
    if products.get(name) < 200:
        product1[name] = products.get(name)
print(product1)


#product1 = {}
for p,v in products.items():
    if v < 200:
        product1.update({p:v})
print(product1)

product2 = {p:v for p,v in products.items() if v < 200}
print(product2)