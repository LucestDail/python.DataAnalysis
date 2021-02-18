# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:48:56 2021
selenium4
@author: dhtmd
"""

from selenium import webdriver
url = "http://www.naver.com/"
driver = webdriver.Chrome("C:/Users/dhtmd/Documents/pythonRepo/python.DataAnalysis/20210218/chromedriver")
driver.get(url)

driver.save_screenshot("naverhome.png")
driver.quit()