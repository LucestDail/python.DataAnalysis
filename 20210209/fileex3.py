'''
Created on Tue Feb  9 08:32:11 2021
@author: myung
fileex3.py : 파일 존재 여부 확인 하기
'''
import os.path  # 파일의 정보관련 모듈

#file = 'C:\\Data\\Python\\nofile.txt'
file ="regularex3.py"  #상대 경로
#file ="c:\\hadoophome" #절대 경로
if os.path.isfile(file):  #file 파일?
    print("Yes. it is a file")
elif os.path.isdir(file):  #file 폴더?
    print("Yes. it is a directory")
    
if os.path.exists(file): #존재?
    print("Something exist")
else :
    print("Nothing")
    
print(os.path.basename(file))
    