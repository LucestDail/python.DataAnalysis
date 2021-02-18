# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:40:08 2021
exam2.py : 대륙 코드를 입력받아 대륙별 레코드만 파일로 저장하기
@author: dhtmd
"""
import pandas as pd


con_code = input("대륙 코드를 입력하세요 : ")
file_path = "drinks.csv"
df = pd.read_csv(file_path)
print(df)
con_list = df.loc[df['continent'] == con_code]
print(con_list)
con_list.to_csv(con_code+".csv",index=False)