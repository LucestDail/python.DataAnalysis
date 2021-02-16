# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:51:27 2021

@author: dhtmd
"""

import pandas as pd
infile = "sales_2015.xlsx"
df = pd.read_excel(infile,sheet_name=None, index_col=None)
row_output = [] #모든 sheet의 데이터 저장
#df.items() : sheet의 정보들
# worksheet_name : sheet 이름
# data : sheet의 데이터
for worksheet_name, data in df.items():
    print("===", worksheet_name, "===")
    row_output.append(data[data["Sale Amount"].replace("$","").replace(",","").astype(float) > 200.0])
    """
    pd.concat : row_output 를 여러개의 데이터를 연결하기
    axis = 0 : row에 연결
    axis : column에 연결
    """
filtered_row = pd.concat(row_output,axis=1, ignore_index=True)
#filtered_row : 모든 sheet의해서 주어진 조건을 데이터 저장
writer = pd.ExcelWriter("sales_all_2015.xlsx",engine="openpyxl")
filtered_row.to_excel(writer, sheet_name="sale_2015",index=False)
writer.save()