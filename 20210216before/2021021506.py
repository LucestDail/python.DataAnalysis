# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:48:39 2021

@author: dhtmd
"""

import pandas as pd

df = pd.DataFrame({"A":[1,4,7],"B":[2,5,8],"C":[3,6,9]})
print(df)
print(df["A"])

print("행의 인덱스 값으로 조회하기")
print("df.iloc[0] = ",df.iloc[0])
print("df.iloc[1] = ",df.iloc[1])
print("df.iloc[2] = ",df.iloc[2])

print("df.loc[0] = ", df.loc[0])
print("df.loc[1] = ", df.loc[1])
print("df.loc[2] = ", df.loc[2])

df = pd.DataFrame(data = ([[1,2,3],[4,5,6],[7,8,9]]),index=[2,"A",4],columns=[51,52,54])
print(df)