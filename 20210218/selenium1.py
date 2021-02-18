# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:44:44 2021

@author: dhtmd
"""

from selenium import webdriver
import time
driver = webdriver.Chrome("C:/Users/dhtmd/Documents/pythonRepo/python.DataAnalysis/20210218/chromedriver")
driver.get("http://python.org")
menus = driver.find_elements_by_css_selector("#top ul.menu li")
print(type(menus))

pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.tag_name,m.text)
pypi.click()
time.sleep(5)
driver.quit()