# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:48:42 2021

@author: dhtmd
"""
print("=============1============")
mylist=[1,2,3,4,5]
add=lambda num:num+10
mylist=list(map(add,mylist))
print(mylist)
print("=============2============")
mylist=list(map(lambda num:num-10,mylist))
mylist=list(map(lambda num:num*10,mylist))
print(mylist)
print("=============3============")
list1=[1,2,3,4]
list2=[10,20,30,40]
hap=lambda n1,n2:n1+n2
haplist=list(map(hap,list1,list2))
print(haplist)
print("=============4============")
list1.append(0)
list2.append(2)
haplist=list(map(lambda n1,n2,n3:n1+n2+n3,mylist,list1,list2))
print(haplist)