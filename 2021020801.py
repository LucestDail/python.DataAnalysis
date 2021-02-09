# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:48:54 2021

@author: dhtmd
"""

num1 = input("value 1 input : ")
num2 = input("value 2 input : ")

try:
    num1 = int(num1)
    num2 = int(num2)
    while True:
        result = num1 / num2
        print(result)
except ValueError  as e: 
    print("ValueErrorException")
    print(e)
except ZeroDivisionError as e: 
    print("ZeroDivisionErrorException")
    print(e)
except KeyboardInterrupt as e: 
    print("KeyBoardInterruptException")
    print(e)
finally:
    print("program exit")