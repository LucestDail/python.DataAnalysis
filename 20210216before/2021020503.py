# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:44:43 2021
aa, bb 리스트 생성
aa 리스트는 0부터 짝수 100개 저장
bb 리스트는 aa 배열 역순으로 값 저장
aa[0] ~ aa[9]
bb[99] ~ bb[90] 값 출력
@author: dhtmd
"""
aa = []
bb = []
for i in range(0,100,1):
    aa.append(i*2)
for i in range(99,-1,-1):
    bb.append(aa[i])

for i in range(0,10,1):
    print(f"aa[{i}] : {aa[i]}")
    
for i in range(99,90,-1):
    print(f"bb[{i}] : {bb[i]}")