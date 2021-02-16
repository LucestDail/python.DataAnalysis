from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def clickImage(event) :
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")

## 메인 코드 부분 ##
window = Tk()  #윈도우 생성
window.geometry("400x400")

photo = PhotoImage(file = "gif/rabbit.gif") #이미지 메모리에 로드
label1 = Label(window, image = photo)

#이벤트 등록:label1 객체를 클릭하면 clickImage함수 호출
label1.bind("<Button>", clickImage)
#label1 윈도우에 추가.
label1.pack( expand = 1, anchor = CENTER)
window.mainloop() #화면에 출력. 표시.

