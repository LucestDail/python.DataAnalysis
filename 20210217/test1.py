# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:17:19 2021
흠...
1.http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp    의 내용을 받아서 forcast.xml 파일로 저장하기.
2. 저장된 파일을 읽어서 다음 결과가 나오도록 프로그램 구현하시오. 
단 결과는 실시간 자료이므로 동일하게  나오지 않습니다.
형태만 맞춰 주시면 됩니다.
[결과]
+ 구름많음
  |- 서울
  |- 인천
  |- 수원
  |- 파주
  |- 이천
  |- 평택
  |- 강릉
+ 흐림
  |- 춘천
  |- 원주
+ 맑음
  |- 대전
  |- 세종
  |- 홍성
  |- 청주
  |- 충주
  |- 영동
  |- 광주
  |- 목포
  |- 여수
  |- 순천
  |- 광양
  |- 나주
  |- 전주
  |- 군산
 ...
@author: dhtmd
"""

from bs4 import BeautifulSoup
import urllib.request as req
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
soup_to_string = str(soup)
f = open("forcast.xml", 'w')
f.write(soup_to_string)
f.close()
fp = open("forcast.xml",mode="r",encoding="euc-kr")
soup = BeautifulSoup(fp,"html.parser")
weather_list = []
for location in soup.find_all('location'):
    weather = location.find('wf').string
    if weather in weather_list:
        pass
    else:
        weather_list.append(weather)

for i in weather_list:
    print("+ ",i)
    for location in soup.find_all('location'):
        if location.find('wf').string == i:
            print(" |-",location.find('city').string)

"""
title = soup.find("title").string
wf = soup.find("wf").string
"""