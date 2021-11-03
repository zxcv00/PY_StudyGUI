from tkinter import *

root = Tk()
root.title("STUDY GUI")

btn1 = Button(root, text = "button 1")
btn1.pack()

# 글자수만큼 버튼의 크기가 늘어난다
btn2 = Button(root, padx = 5, pady = 10, text = "button 2")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "button 3")
btn3.pack()

# 버튼의 넓이와 높이를 지정한다 (변경 불가능)
btn4 = Button(width = 10, height = 3, text = "button 4")
btn4.pack()

btn5 = Button(root, fg = "red", bg = "yellow", text = "button 5")
btn5.pack()

photo = PhotoImage(file = "STUDY_GUI/GUI_BASIC/img.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("button click!")

btn7 = Button(root, text = "동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()