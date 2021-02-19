# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:38:06 2021

@author: dhtmd
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import rc
rc('font',family="Malgun Gothic")

CCTV_Seoul = pd.read_csv("CCTV_in_Seoul.csv", encoding="utf-8")
print(CCTV_Seoul)
pop_Seoul = pd.read_excel("population_in_Seoul.xls", header = 2, usecols="B, D, G, J, N")
print(pop_Seoul)
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : "구별"}, inplace=True)
print(CCTV_Seoul.head())
pop_Seoul.rename(columns={
    pop_Seoul.columns[0] : "구별",
    pop_Seoul.columns[1] : "인구수",
    pop_Seoul.columns[2] : "한국인",
    pop_Seoul.columns[3] : "외국인",
    pop_Seoul.columns[4] : "고령자"}, inplace=True)
print(pop_Seoul.head())
pop_Seoul.drop([0],inplace=True)
print(pop_Seoul.head())

print(pop_Seoul[pop_Seoul["구별"].isnull()])
pop_Seoul.drop([26], inplace=True)
print(pop_Seoul)

pop_Seoul["외국인 비율"] = 100*pop_Seoul["외국인"] / pop_Seoul["인구수"]

pop_Seoul["고령자 비율"] = 100*pop_Seoul["고령자"] / pop_Seoul["인구수"]
print(pop_Seoul)

CCTV_Seoul["최근 증가율"] = 100 * (CCTV_Seoul["2014년"] + CCTV_Seoul["2015년"] + CCTV_Seoul["2016년"]) / CCTV_Seoul["2013년도 이전"]
print(CCTV_Seoul.head())


data_result = pd.merge(CCTV_Seoul, pop_Seoul, on="구별")
print(data_result.info())
print(data_result)
left = pd.DataFrame({"key":["K0","K4","K2","K3"],"A" : ["A0","A1","A2","A3"], "B" : ["B0","B1","B2","B3"]})
right = pd.DataFrame({"key":["K0","K1","K2","K3"],"C" : ["C0","C1","C2","C3"], "D" : ["D0","D1","D2","D3"]})
leftright = pd.merge(left, right, on="key")
print(left)
print(right)
print(leftright)

data_result.set_index("구별", inplace=True)
print(data_result.head())

plt.figure()
#data_result["소계"].plot(kind="barh", grid=True, figsize=(10,10))
#data_result["소계"].sort_values().plot(kind="barh", grid=True, figsize=(10,10))
#CCTV_rate = 100*data_result["소계"]/data_result["인구수"]
#CCTV_rate.sort_values().plot(kind="barh", grid=True, figsize=(10,10))

data_result["CCTV비율"] = data_result["소계"]/data_result["인구수"]*100
data_result["CCTV비율"].sort_values().plot(kind="barh", grid=True, figsize=(10,10))
plt.figure(figsize=(6,6))
plt.scatter(data_result["인구수"],data_result["소계"],s=50)
plt.xlabel("인구수")
plt.ylabel("CCTV")
plt.grid()

fp1 = np.polyfit(data_result["인구수"],data_result["소계"],1)
f1 = np.poly1d(fp1)
fx = np.linspace(100000,700000,100)

plt.figure(figsize=(10,10))
plt.scatter(data_result["인구수"], data_result["소계"], s=50)
plt.plot(fx, f1(fx), ls="dashed", lw=3, color="g")
plt.xlabel("인구수")
plt.ylabel("CCTV")
plt.grid()
plt.show()