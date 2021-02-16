# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:00:01 2021

@author: myung

20210210/guiex6.py : GUI 환경에서 db 내용 조회하기
"""
import sqlite3
from tkinter import *
from tkinter import messagebox
"""
    edit1~ edit4의 입력란의 값을 db에 저장하기
    등록성공/실패 시 성공/실패 메세지를 messagebox로 표시하기 => 예외처리필요.
"""
def insertData() :
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""     
    con = sqlite3.connect("../20210209/iddb")
    cur = con.cursor()    
    data1 = edit1.get()
    data2 = edit2.get()
    data3 = edit3.get() 
    data4 = edit4.get()
    try :
        sql = "insert into usertable values ('" \ 
     + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
        cur.execute(sql)
    except : #try 구문에서 오류 발생시 실해되는 블럭 
        messagebox.showerror("오류", "데이터 입력 오류 발생")
    else : #정상적인 경우만 실행 되는 블럭
        messagebox.showinfo("성공", "데이터 입력 성공")
    finally: #정상, 오류 모두 실행되는 블럭   
        con.commit()
        con.close()
    
def selectData() :
    strData1, strData2, strData3, strData4 = [], [], [], []
    # usertable 테이블이 존재하는 sqlite 데이터 베이스 파일을 설정 
    con = sqlite3.connect("../20210209/iddb")
    cur = con.cursor()
    cur.execute("select * from usertable")
    #각각의 리스트에 head 부분 표시
    strData1.append("사용자ID");    strData2.append("사용자이름");
    strData3.append("이메일");      strData4.append("출생년도");
    strData1.append("-----------");    strData2.append("-----------");
    strData3.append("-----------");    strData4.append("-----------");
    
    while True :
        row = cur.fetchone() #레코드 한개씩 읽기 
        if row == None :
            break;
        strData1.append(row[0]);  #사용자아이디
        strData2.append(row[1]);  #사용자이름
        strData3.append(row[2]);  #이메일
        strData4.append(row[3]);  #생일년도
    #ListBox의 기존 내용을 제거 0인덱스에서 마지막인데스까지 내용 제거
    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)
    listData4.delete(0, listData4.size() - 1)
  
   #zip(strData1, strData2, strData3, strData4)  => 같은크기의 리스트 결합
   #item1 : strData1의 한개의 요소 : 사용자아이디값
   #item2 : strData2의 한개의 요소 : 사용자이름값
   #item3 : strData3의 한개의 요소 : 이메일값
   #item4 : strData4의 한개의 요소 : 생일년도값

    for item1, item2, item3, item4 in \
                      zip(strData1, strData2, strData3, strData4) :
        #listBox 칸의 마지막에 데이터를 추가하기                            
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
    con.commit()
    con.close()  
    
    

window = Tk()  
window.geometry("1000x500")
window.title("GUI 데이터 입력")

edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edit1 = Entry(edtFrame, width=10) 
edit1.pack(side=LEFT, padx=10, pady=10)
edit2 = Entry(edtFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)
edit3 = Entry(edtFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)
edit4 = Entry(edtFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(edtFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect = Button(edtFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

listData1 = Listbox(listFrame, bg="yellow")
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg="yellow")
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg="yellow")
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg="yellow")
listData4.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()