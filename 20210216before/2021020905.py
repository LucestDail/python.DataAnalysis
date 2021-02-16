# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:40:23 2021

@author: dhtmd
"""

import os.path # 파일 정보 관련 모듈

#file = 'C:\\Data\\Python\\nofile.txt'
file = "2021020904.py"
if os.path.isfile(file):
    print("file")
elif os.path.isdir(file):
    print("dir")
if os.path.exists(file):
    print("exist")
else:
    print("None")
    
print(os.path.basename(file))