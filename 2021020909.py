# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:05:52 2021

@author: dhtmd
"""

import sqlite3

con, cur = None, None
row = None
con = sqlite3.connect("iddb")
cur = con.cursor()


cur.execute("select * from usertable")
item_list = cur.fetchall()
for it in item_list:
    print(it)
print()

cur.execute("select * from usertable")
while True:
    row = cur.fetchone()
    if row == None:
        break
    print("%5s %15s %15s %d" %(row[0], row[1], row[2], row[3]))
con.close()

conn = sqlite3.connect("iddb")
cur = conn.cursor()
cur.execute("select * from usertable")
user_list = cur.fetchall()
print(type(user_list))
for it in user_list:
    print(it)