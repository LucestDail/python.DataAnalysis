# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:35:19 2021

@author: dhtmd
"""

import sqlite3

data = [('test2','테스트2','test2@bbb.ccc','1990'),('test3','테스트3','test3@bbb.ccc','1993'),('test4','테스트4','test4@bbb.ccc','1994')]
con = sqlite3.connect("iddb")
cur = con.cursor()
cur.executemany("insert into usertable (id, username, email, birthyear) values (?,?,?,?)", data)
con.commit()

cur.execute("select * from usertable")
item_list = cur.fetchall()
for it in item_list:
    print(it)
print()

con.close()