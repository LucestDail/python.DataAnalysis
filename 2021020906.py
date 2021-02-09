# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:51:27 2021

@author: dhtmd
"""

import os.path

print("폴더 목록 보기 : os.walk 모듈 사용")
for dirName, subDirList, fnames in os.walk("c:\\hadoophome"):
    for fname in fnames:
        print(os.path.join(dirName, fname))
    print(type(subDirList))
    print(subDirList)