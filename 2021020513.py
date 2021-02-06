# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:09:36 2021

@author: dhtmd
"""

def func1():
    global gval
    a = 20
    b = 1000
    gval = 200
    print(f"func1 invoke {a} {b} {gval}")
    
def func2():
    print("func2 invoke func1")
    func1()
    print(f"gval : {gval} {a}")

gval = 100
a = 10

if __name__ == '__main__':
    func2()