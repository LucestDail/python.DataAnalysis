# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:14:33 2021

@author: dhtmd
"""

time = int(input("시간 입력 : "))
print(f"hour : {time//3600}")
time = time%3600
print(f"minute : {time//60}")
print(f"sec: {time%60}")