# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:41:59 2021

@author: dhtmd
"""

from bs4 import BeautifulSoup
import urllib.request as req
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser",from_encoding="utf-8")
sel = lambda q : soup.select(q)
hlist = sel("div.head_info")#class 속성이 head_info div 태그들
htitle = sel("h3.h_lst")#class 속성이 h_lst 속성 가져올
for tag, title in zip(hlist, htitle): #zip? 
    print(title.select_one("span.blind").string, end=" \t")#통화명
    value = tag.select_one("span.value").string#환율 정보
    print(value,end=" \t")
    change=tag.select_one("span.change").string#변동값
    print(change, end=" \t")
    blinds = tag.select("span.blind")#상승,하락
    b = tag.select("span.blind")[-1].string#가장 마지막 태그 선
    print(b,end="*******\n")