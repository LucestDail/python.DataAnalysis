# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:32:06 2021

@author: dhtmd
"""

import pandas as pd
infile = "sales_2015.xlsx"
outfile = "sales_2015_pd.xlsx"
#read_excel(file이름, sheet 이름, 인덱스 칼럼 여부)
df = pd.read_excel(infile,"january_2015",index_col=None)
print(df)
#df_value : Sale Amount 컬럽의 값이 500.0 보다 큰 값을 가지는 행을 조회
df_value = df[df["Sale Amount"].astype(float) > 500.0]
#xlsx 파일로 저장
#writter : sales_2015_pd.xlsx 파일을 출력 파일로 설정. openpyxl => xlsx 형태
writer = pd.ExcelWriter(outfile,engine="openpyxl")
#df_value의 데이터를  writer 파일에 jan_15_out sheet로 저장, 인덱스값 없
df_value.to_excel(writer,sheet_name="jan_15_out",index=False)
writer.save()