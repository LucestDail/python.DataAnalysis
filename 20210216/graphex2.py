# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:54:35 2021

@author: dhtmd
"""

import matplotlib.pyplot as plt
import numpy as np
"""
2행2열 분리
ax_lst : 이미지 목록
fig : 분리된 도화지
"""
fig, ax_lst = plt.subplots(2,2,figsize=(8,5))
fig.suptitle('figure sample plos')
#0행 0열 그래프
ax_lst[0][0].plot([1,2,3,4])
#np.random.randn : 정규분포에 맞도록 난수
ax_lst[0][1].plot(np.random.randn(4,10),np.random.randn(4,10))
#
ax_lst[1][0].plot(np.linspace(0.0, 5.0), np.cos(2*np.pi*np.linspace(0.0,5.0)))
ax_lst[1][1].plot([3,7],[5,4])
plt.show()