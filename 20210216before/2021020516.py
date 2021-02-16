# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:04:33 2021

@author: dhtmd
"""

my_list = [1,2,3,4,5]
def add10(num):
    return num+10

for i in range(len(my_list)):
    my_list[i] = add10(my_list[i])
    
    
print(my_list)

add = lambda num:num+10
for i in range(len(my_list)):
    my_list[i] = add(my_list[i])
    
print(my_list)