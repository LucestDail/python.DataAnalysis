# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:29:19 2021

@author: myung

exam3.py : 리스트의 값의 합과 평균을 구하는 함수 작성하기
"""
#sum(list) : list의 요소의 합계 리턴 
def getMean(numlist):
#    if len(numlist) > 0 :
#        return sum(numlist) / len(numlist)
#    else :
#        return 0        
     return sum(numlist) / len(numlist) if len(numlist)>0 else 0

def getSum(numlist):
    return sum(numlist)


list= [2,3,3,4,4,5,5,6,6,8,8]
print("list의 값의 합 :", getSum(list))
print("list의 값의 평균 :", getMean(list))

list2 = []
print("list2의 값의 합 :", getSum(list2))
print("list2의 값의 평균 :", getMean(list2))

tp= (2,3,3,4,4,5,5,6,6,8,8)
print("tp의 값의 합 :", getSum(tp))
print("tp의 값의 평균 :", getMean(tp))
