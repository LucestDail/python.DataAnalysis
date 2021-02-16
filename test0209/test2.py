# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:13:03 2021

@author: myung

test2.py : 스레드로 합구하기
"""
import threading

class Sum :
    startnum = 0
    endnum = 0
    sum=0
    def __init__(self, snum,enum) :
        self.startnum = snum
        self.endnum = enum
        
    def getSum(self) :  
        for i in range(self.startnum,self.endnum+1) :
            self.sum += i
        return self.sum
    
if __name__ == "__main__" :
    sumlist = []
    thlist = []
    for i in range(0,5) :
      sumlist.append(Sum((i*2000)+1,(i+1)*2000))
      thlist.append(threading.Thread(target=sumlist[i].getSum))
      thlist[i].start()
      
    for th in thlist:
      th.join()
      
    sum=0  
    for s in sumlist:
        sum += s.sum
        
    print(sum)    
      
         