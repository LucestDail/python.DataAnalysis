# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:08:43 2021
격자모양
@author: dhtmd
"""

import numpy as np
import matplotlib.pyplot as plt

xvalue = np.linspace(0,10,11) #0 ~ 10 균등 분포 11개 숫자
yvalue = np.linspace(0,10,11)
#np.meshgrid : 2차원 형태로 저
x,y = np.meshgrid(xvalue,yvalue)
print(x)
print(y)
plt.figure()
plt.scatter(x,y,s=100,c="b")
plt.xlim(0,10)
plt.ylim(0,10)
plt.show()