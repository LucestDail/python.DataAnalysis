# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:41:48 2021
csvex1.py : csv 파일 읽기 => 파일 복사하기
run -> configuration per file -> commandline 추가(jeju.csv jeju_out.csv)
@author: dhtmd
"""

from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("좋아하는 동물 사진 보기")

def myFunc():
    if var.get() == 1:
        labelImage.configure(image=photo1)
    elif var.get() == 2:
        labelImage.configure(image=photo2)
    else:
        labelImage.configure(image=photo3)
        
labelText = Label(window, text="좋아하는 동물 투표", fg="blue", font=("궁서체"))

var = IntVar()
rb1 = Radiobutton(window, text="강아지", variable=var, value = 1)
rb2 = Radiobutton(window, text="고양이", variable=var, value = 2)
rb3 = Radiobutton(window, text="토끼", variable=var, value = 3)
buttonOk = Button(window,text="사진 보기", command=myFunc)

photo1 = PhotoImage(file="GIF/dog.gif")
photo2 = PhotoImage(file="GIF/cat.gif")
photo3 = PhotoImage(file="GIF/rabbit.gif")

labelImage = Label(window, width=200, height=200, bg="yellow", anchor="center")
labelText.pack(padx=5, pady=5)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
buttonOk.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)
window.mainloop()