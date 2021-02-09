# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:32:20 2021

@author: dhtmd
"""

outfp = None
outfp = open("data.txt","w",encoding="UTF8")
while True:
    outStr = input("input value : ")
    if outStr != "":
        outfp.writelines(outStr + "\n")
    else:
        break
outfp.close()
print("EOP")