# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:13:13 2021

sales_2015.xlsx파일에서
sheet=january_2015인 sheet의 Customer Name 컬럼의 값이 J로 시작하는 행만 선택하여 
sale_2015_J sheet 이름으로 sale_2015_J.xlsx 파일 저장하기

@author: dhtmd
"""

import pandas as pd
infile = "sales_2015.xlsx"
df = pd.read_excel(infile,sheet_name="january_2015", index_col=None)
df_value=df[df["Customer Name"].str.startswith("J")]
writer = pd.ExcelWriter("sales_2015_J.xlsx",engine="openpyxl") 
df_value.to_excel(writer, sheet_name="sales_2015_J",index=False)  
writer.save()
