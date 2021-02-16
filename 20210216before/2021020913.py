# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:15:36 2021

@author: dhtmd
"""

import threading # 스레드 모듈
import time # 스레드 대기 기능 모듈

class RacingCar:
    carName = ""
    def __init__(self, name):
        self.carName = name
    def runCar(self):
        for _ in range(0,3):
            carStr = self.carName + "달립니다.\n"
            print(carStr,end="")
            time.sleep(0.1) # 0.1초 대기
            
car1 = RacingCar("자동차1")
car2 = RacingCar("자동차2")
car3 = RacingCar("자동차3")
th1 = threading.Thread(target=car1.runCar)
th2 = threading.Thread(target=car2.runCar)
th3 = threading.Thread(target=car3.runCar)
th1.start() 
th2.start()
th3.start()
th1.join()
th2.join()
th3.join()
print("main 종료")