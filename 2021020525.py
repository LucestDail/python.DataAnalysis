# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:53:30 2021

@author: dhtmd
"""

def even_sum(target):
    even_sum_total = 0
    for i in range(0,target):
        if(i%2 ==1):
            even_sum_total += i
        if(even_sum_total >= 1000):
            return even_sum_total
        
print(even_sum(1000))