# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021
@author: myung

mod2.py : 모듈로 import됨. 
          실행도 됨.
"""
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b
'''
__name__  : mod2.py 파일을 실행할 경우 "__main__" 값이 저장됨.
''' 
if __name__ =="__main__":  #mod2.py 파일이 직접실행시 
    print(add(3, 4))
    print(sub(4, 2))
