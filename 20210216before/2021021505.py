# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:40:31 2021
pandas 이용하여 csv 파일 읽기
@author: dhtmd
"""

import pandas as pd
infile = "jeju1.csv"
df = pd.read_csv(infile)
print(df)
print(type(df))

print(df["LON"])
print(df["LAT"])
print(df["장소"])

print(df.iloc[3])