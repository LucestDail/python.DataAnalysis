# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:10:47 2021

@author: dhtmd
"""

import pandas as pd

infile = "supplier_data.csv"
df = pd.read_csv(infile)
print(df)

importdate = ["1/20/14", "1/30/14"]
#isin : 주어진 값이 맞는지? boolean 값으로 리턴
print(df["Purchase Date"].isin(importdate))
df_inset = df.loc[df["Purchase Date"].isin(importdate),:]
print(df_inset)
print(df["Invoice Number"].str.startswith("920-"))
df_inset = df.loc[df["Invoice Number"].str.startswith("920-")]
print(df_inset)
print(type(df_inset))
df_inset.to_csv("pandas_oout3.csv",index=False)