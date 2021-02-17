# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:38:02 2021

@author: dhtmd
"""

import json
price = {
        "date" : "2021-02-17",
        "price" : {
            "Apple" : 800,
            "Orange" : 1000,
            "Banana" : 500
            }
        }
print("날짜 : ",price["date"])
for p in price["price"].keys():
    print("%s => %s" % (p,price["price"][p]))
json.dump(price,open("price.json","w"))

print()
str = """{
        "date" : "2021-02-17",
        "price" : {
            "Apple" : 800,
            "Orange" : 1000,
            "Banana" : 500
            }
        }
    """
pri = json.loads(str)
print("날짜 : ",pri["date"])
for p in pri["price"].keys():
    print("%s => %s" % (p,pri["price"][p]))
json.dump(pri,open("price2.json","w"))