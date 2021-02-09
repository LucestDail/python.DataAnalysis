# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:14:58 2021

@author: dhtmd
"""

numbers = []
for n in range(1,11):
    numbers.append(n)
print(numbers)

print([x for x in range(1,11)])
clist=[x for x in range(1,11)]
print(clist)

evenlist = []
for n in range(1,11):
    if n%2==0:
        evenlist.append(n)
print(evenlist)

evenlist=[x for x in range(1,11) if x%2==0]
print(evenlist)

list23=[x for x in range(1,11) if x%2==0 if x%3==0]
print(list23)

matrix = [[1,2,3],[4,5,6],[8,9,0]]
print(matrix)
list1 = [x for row in matrix for x in row]
print(list1)

list1=[]
for row in matrix:
    for x in row:
        list1.append(x)
print(list1)

colorlist=['black','white','blue']
sizelist=["s","m","l"]
dresslist=((c,s) for c in colorlist for s in sizelist)
for d in dresslist:
    print(d)