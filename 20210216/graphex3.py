# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:10:48 2021

@author: dhtmd
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("ggplot")
#1행 2열 영역 분리
fig, axes = plt.subplots(nrows=1, ncols=2)
ax1, ax2 = axes.ravel()
#np.random.rand(5,3) : 5행 3열 만큼 난수 저장, 0 ~ 1 사이 값 저장
data_frame = pd.DataFrame(np.random.rand(5,3),index=["Customer 1","Customer 2","Customer 3","Customer 4","Customer 5"],columns=pd.Index(["Matric 1","Matric 2","Matric 3"], name="Metrics"))
print(data_frame)
data_frame.plot(kind="bar", ax=ax1, alpha=0.75, title="Bar plot")
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
ax1.set_xlabel("Customer")
ax1.set_ylabel("Value")
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")

#data_frame 데이터로 막대 그래프 작성
colors = dict(boxes="DarkBlue",whiskers="Gray",medians="Red",caps="Black")
data_frame.plot(kind="box",color=colors,sym="r.", ax=ax2, title="Box Plot")
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
ax2.set_xlabel("Metric")
ax2.set_ylabel("Value")
ax2.xaxis.set_ticks_position("bottom")
ax2.yaxis.set_ticks_position("left")