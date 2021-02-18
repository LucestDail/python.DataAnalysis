# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:17:19 2021

@author: dhtmd
"""

import time
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/dhtmd/Documents/pythonRepo/python.DataAnalysis/20210218/chromedriver")
time.sleep(5)
driver.get("https://devosh.herokuapp.com/admin")
id = "admin"
driver.execute_script("document.getElementsByName('username')[0].value='"+id+"'")
pw = "1234"
driver.execute_script("document.getElementsByName('password')[0].value='"+pw+"'")
driver.submit()