# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:20:55 2021

@author: dhtmd
"""

import matplotlib.pylab as plt
from matplotlib import rc
rc('font', family="Malgun Gothic")

labels = ['개구리','돼지','개','통나무'] #라벨
sizes = [15,30,45,10] #사이즈
colors = ['yellowgreen','gold','lightskyblue','lightcoral'] #색깔
explode = (0,0.1,0,0) #떨어트림
plt.title("Pie Chart")

#width : 깊이, linewidth : 테두리
wedgeprops = {'width' : 0.7, 'edgecolor':'w','linewidth':0}
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops=wedgeprops)
plt.show()