# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:35:03 2021

@author: myung
dbex4.py : usertable 에 데이터 추가하기
"""
import sqlite3

data=[('test2','테스트2','test2@aaa.bbb',1991),
      ('test3','테스트3','test3@aaa.bbb',1993),
      ('test4','테스트4','test4@aaa.bbb',1994),
      ('test5','테스트5','test5@aaa.bbb',1995)]
#data : 리스트
con = sqlite3.connect("iddb")
cur = con.cursor()
cur.executemany("""insert into usertable 
    (id,username,email,birthyear) values (?,?,?,?)""",data)
con.commit();

cur.execute("select * from usertable")
item_list = cur.fetchall()
for it in item_list :
   print(it)
print() 

con.close()