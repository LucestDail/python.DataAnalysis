# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:01:34 2021
selenium3.py 셀리니움 이용 url 연결
url 제공되는 html 내용을 beautifulSoup 모듈로 파싱
pandas 모듈을 이용하여 csv 파일로 생성
@author: dhtmd
"""

import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome("C:/Users/dhtmd/Documents/pythonRepo/python.DataAnalysis/20210218/chromedriver")
driver.get("https://oscar.go.com/winners")

time.sleep(1)
html = driver.page_source
print(type(html))
soup = BeautifulSoup(html,'html.parser')
category = soup.select('bls-winners-list > ul > li > div.winners-list__info > a')


movie = soup.select('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select('bls-winners-list > ul > li > div.winners-list__info > p')
print("category : ",type(category))
print("movie : ",type(movie))
print("producer : ",type(producer))

oscars_2020=[]
for item in zip(category,movie, producer):
    oscars_2020.append(
        {
            'categoru' : item[0].text,
            'movie' : item[1].text,
            'producer' : item[2].text
            }
        )
data = pd.DataFrame(oscars_2020)
print(data)
data.to_csv('oscars_win_2020.csv',index=False)
driver.quit()