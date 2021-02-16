# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:01:23 2021

@author: dhtmd
"""

from tkinter import *
from tkinter.filedialog import *

def func_open():
    #파일 열기 창 열기
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일","*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit() # 윈도우 객체 보이지 않도록 하기
    window.destroy() # 윈도우 객체 제거하고 프로그램 종료
    
window = Tk()
window.geometry("400x400")
window.title("GIF 이미지 선택하여 보기")
photo = PhotoImage() #이미지 설정 안함
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command=func_exit)

window.mainloop()