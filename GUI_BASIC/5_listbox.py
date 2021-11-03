from tkinter import *

root = Tk()
root.title("STUDY GUI")
root.geometry("640x480")

# 여러 줄에 걸쳐 목록을 관리하는 위젯
listbox = Listbox(root, selectmode = "extended", height = 0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0)     # 맨 앞 항목 삭제

    # 개 수 확인
    # print("list count => ", listbox.size())

    # 항목 확인 (시작 index, 마지막 index)
    print("1 ~ 3 => ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환 ex) 1, 2, 3)
    print("selected item => ", listbox.curselection())


btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop()