# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:07:41 2021

@author: dhtmd
"""

import json
import os.path
import urllib.request as req

url = "https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(savename): #repo.json 파일이 없으면
    req.urlretrieve(url,savename) #url 에서 전달된 내용을 파일로 저장해

items = json.load(open(savename,"r",encoding="utf-8"))
print(type(items))
for item in items:
    print(type(item))
    print(item["name"] + "-" + item["owner"]["login"])
json.dump(items,open("json_output.json","w",encoding="utf-8"))