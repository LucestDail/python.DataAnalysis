# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:09:17 2021

@author: dhtmd
"""

import matplotlib.pyplot as plt #pip3 install ggplot

plt.style.use("ggplot")
subjects = ["Java", "JSP","SPRING","HADOOP","Python"]#막대그래프 x 좌표값
print(range(len(subjects)))
subjects_index = range(len(subjects)) #subjects_index : 0 ~ 4 값을 저장
print(type(subjects))
scores = [65,90,85,60,95]#막대그래프로 표현할 값
#그래프 출력
fig = plt.figure()#그래프 그릴 수 있는 그래프 공간, 도화지
#그래프 공간 분리, 하나의 도화지에 여러개의 그림 가능
# 1행 1열 분리 => 한개 그림, 분리 안함.
# 1:1번째 그림
# ax1 : 그래프가 그려지는 영역
ax1 = fig.add_subplot(1,1,1)
"""
ax1.bar : 막대그래프
subjects_index : x 좌표 내용 인덱스
scores : 막대그래프로 표현할 데이터 값
"""
ax1.bar(subjects_index,scores,align="center",color="darkblue")
"""
xaxis : x축 위치
yaxis : y축 위치
"""
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
"""
xticks : x축
rotation : x축에 표시되는 내용의 방향
"""
plt.xticks(subjects_index, subjects, rotation=0,fontsize="small")
#x축 제목
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")
#메모리에 저장된 이미지를 파일로 생성
plt.savefig("bar_plot.png",dpi=400,bbox_inches="tight")
plt.show()