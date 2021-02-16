# -*- coding: utf-8 -*-
"""
list 합

Created on Fri Feb  5 10:12:43 2021

@author: dhtmd
"""

my_list = [30,20,10]
print(f"my_list : {my_list}")
my_list.append(40)
print(f"my_list.append(40) : {my_list}")
print(f"my_list.pop() : {my_list.pop()}")
my_list.sort()
print(f"my_list.sort() : {my_list}")
my_list.reverse()
print(f"my_list.reverse() : {my_list}")

print(f"my_list.index(20) : {my_list.index(20)}")
my_list.insert(2,222)
print(f"mylist.insert(2,222) : {my_list}")
my_list.remove(222)
print(f"my_list.remove(222) : {my_list}")
my_list.extend([77,77,99])
print(f"my_list.extend([77,77,99]) : {my_list}")
print(f"my_list.count(77) : {my_list.count(77)}")