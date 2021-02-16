# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:32:08 2021

@author: myung

ifex1.py : if 구문 연습
"""
score = 50
if score >= 90:
    print("A학점")
else :
    if score >= 80 :
        print("B학점")
    else :
        if score >= 70 :
            print("C학점")
        else :
            if score >= 60 :
                print("D학점")
            else :    
                print("F학점")
print("if elif 구문 연습")
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")
    
    

