"""
    guiex3.py :메뉴의 파일열기를 통해서 이미지 선택하기
"""
from tkinter import *
from tkinter.filedialog import *

def func_open() :
               #파일 열기 창을 열기.
    filename = askopenfilename(parent = window, 
               filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()  #윈도우 객체 보이지 않도록.
    window.destroy() #윈도우 객체 제거하고, 프로그램 종료
    
window = Tk()
window.geometry("400x400")
window.title("GIF 이미지 선택하여 보기")
photo = PhotoImage()  #이미지 설정 안함.
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window) #Menu 객체 생성
window.config(menu = mainMenu) #window에 menu 설정. 
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator() #중간선 설정
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()