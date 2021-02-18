# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:43:06 2021
drinkdataex2.py : 대륙별 데이터를 분석하여 파이 그래프로 출력
@author: dhtmd
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = "drinks.csv"
drinks = pd.read_csv(file_path)
print(drinks.isnull().sum())
print(drinks.dtypes)

#결측 데이터를 "OT" 값으로 치환
drinks['continent'] = drinks['continent'].fillna('OT')
labels = drinks['continent'].value_counts().index.tolist()
fracs1=drinks['continent'].value_counts().values.tolist()
explode = (0.1, 0, 0, 0, 0, 0)
print(drinks['continent'].value_counts())
print(fracs1)

plt.pie(fracs1, explode=explode, labels=labels, autopct='%.0f%%', shadow=True)
plt.title('null data to \'to\'')
plt.show()