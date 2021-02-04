# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:49:19 2021

@author: dhtmd
"""

inputValue = input("16진수 입력 : ")
try:
    inputNum = int(inputValue,16)
    print(f"{inputValue} = {inputNum}")
except: 
    print(f"{inputValue} 문자는 16진수 문자가 아닙니다.")