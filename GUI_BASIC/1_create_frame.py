from tkinter import *

root = Tk()
root.title("STUDY GUI")

root.geometry("640x480")        # 가로 * 세로
# root.geometry("640x480+100+300")        # 가로 * 세로 + x 좌표 + y 좌표

root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가(창 크기 변경 불가)

root.mainloop()