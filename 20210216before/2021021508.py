# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:50:12 2021

@author: dhtmd
"""

import pandas as pd
infile = "supplier_data.csv"
df = pd.read_csv(infile)

df_col = df.iloc[:,[0,3]] #모든행, 0번 3번 열 조회
print("df.iloc[:,[0,3]] =>")
print(df_col)
df_col = df.iloc[0:4, 0:3]# 0~3 인덱스 0~2 인덱
print("df.iloc[0:4,0:4] =>")
print(df_col)


df_col = df.loc[df["Invoice Number"].str.startswith("920-"),["Invoice Number","Cost"]]
#df_col = df.loc[:,['Invoice Number', 'Cost']]
print(df_col)