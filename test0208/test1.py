# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:28:09 2021

@author: myung
test1.py : 다음 결과를 예측하시오 
"""

a = "Life is too short, you need python"

if "wife" in a:  # false
    print("wife")
elif "python" in a and "you" not in a: # true and false => false
    print("python")
elif "shirt" not in a: # true
    print("shirt")
elif "need" in a: 
    print("need")
else: print("none")