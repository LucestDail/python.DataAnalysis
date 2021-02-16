# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:36:54 2021

@author: dhtmd
"""

singer = {}
singer['name']='twice'
singer['num']=9
singer['song']='like woo-ah'
singer['company']='JYP'
for i in singer.keys():
    print(f"{i} => {singer[i]}")
    
print(f"type(singer) : {type(singer)}")
print(f"singer : {singer}")
print(f"type(singer.keys) : {type(singer.keys())}")
print(f"singer.keys() : {singer.keys()}")