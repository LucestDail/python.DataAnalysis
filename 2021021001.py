# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:31:28 2021

@author: dhtmd
"""

from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")
    
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "GIF/rabbit.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack( expand = 1, anchor = CENTER)
window.mainloop()