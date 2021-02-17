# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:55:04 2021

@author: dhtmd
"""

from bs4 import BeautifulSoup

fp = open("books.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")
print(soup.select("li")[3].string)#li 태그들 중 4번째 태그와 내용 출력
print(soup.find_all("li")[3].string)#li 태그들 중 4번째 태그와 내용 출력

#id 속성이 nu 인 태그 값 출력
print(soup.select_one("li#nu").string)
print(soup.find(id='nu').string)

#ul 태그의 자식 태그인 id 속성이 nu인 li태그의 값 출력
print(soup.select_one("ul>li#nu").string)
print(soup.select_one("ul li#nu").string)
#id 속성 bible 태그 하위 태그 중 id 속성 nu 인 li 태그 값 출력
print(soup.select_one("#bible li#nu").string)
sel = lambda q:print(soup.select_one(q).string)
#id 속성이 nu인 태그 값 출력
sel("#nu")
#id 속성이 nu인 li태그의 값을 출력
sel("li#nu")
#ul 태그의 자식 태그인 id 속성이 nu인 li 태그의 값을 출력
sel("ul>li#nu")
#ul 태그의 하위 태그 중 id 속성이 nu 인 li 태그의 값을 출력
sel("ul li#nu")
#id 속성이 bible 인 태그의 하위 태그 중 id 속성이 nu인 li 태그의 값을 출
sel("#bible li#nu")
#li 태그 중 4번째 태그 값을 출력
sel("li:nth-of-type(4)")
#id 속성이 nu인 li 태그의 값을 출력
sel("li[id='nu']")