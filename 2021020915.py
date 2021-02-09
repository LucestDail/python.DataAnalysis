# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:05:27 2021
2. Thread를 이용하여 

1~10000까지의 합을 5개의 스레드로 나눠서 각각의 구간 합을 

스레드 1 : 1 ~ 2000까지의 합

스레드 2 : 2001 ~ 4000까지의 합

스레드 3 : 4001 ~ 6000까지의 합

스레드 4 : 6001 ~ 8000까지의 합

스레드 5 : 8001 ~ 10000까지의 합

main에서 더하여 총합을 구하는 프로그램 작성하기
@author: dhtmd
"""

import threading # 스레드 모듈
import time # 스레드 대기 기능 모듈

class threadPart:
    startNum = 0
    sumValue = 0
    def __init__(self, startNum):
        self.startNum = startNum
    def sumPart(self):
        for i in range(self.startNum,self.startNum+2000):
            self.sumValue += i
        
    
tp1 = threadPart(1)
tp2 = threadPart(2001)
tp3 = threadPart(4001)
tp4 = threadPart(6001)
tp5 = threadPart(8001)

th1 = threading.Thread(target=tp1.sumPart)
th2 = threading.Thread(target=tp2.sumPart)
th3 = threading.Thread(target=tp3.sumPart)
th4 = threading.Thread(target=tp4.sumPart)
th5 = threading.Thread(target=tp5.sumPart)

th1.start() 
th2.start()
th3.start()
th4.start()
th5.start()
th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
print(th1)
returnValue = 0
print(f"main 종료 : {returnValue}")