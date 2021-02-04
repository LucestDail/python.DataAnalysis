# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:03:22 2021

@author: dhtmd
"""

money = int(input("값 입력 : "))
print(f"500 : {money//500}")
money = money%500
print(f"100 : {money//100}")
money = money%100
print(f"50 : {money//50}")
money = money%50
print(f"10 : {money//10}")
print(f"1 : {money%10}")