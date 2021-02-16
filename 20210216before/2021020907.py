# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:01:19 2021

@author: dhtmd
"""

import sqlite3
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)
cur = conn.cursor()
cur.executescript(
    '''
    drop table if exists items;
    create table items (item_id integer primary key,
                        name text unique,
                        price integer);
    insert into items (name, price) values ('Apple',800);
    insert into items (name, price) values ('Orange',500);
    insert into items (name, price) values ('Banana',300);
    '''
    )

conn.commit()
cur = conn.cursor()
cur.execute("select * from items")
item_list = cur.fetchall()
print(type(item_list))
for it in item_list:
    print(it)