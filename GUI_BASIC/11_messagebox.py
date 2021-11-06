import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("STUDY GUI")
root.geometry("640x480")

# 기차 예매 시스템으로 가정
def info():
    msgbox.showinfo("NOTICE", "예매 완료")

def warn():
    msgbox.showwarning("WARNING", "이미 매진된 좌석")

def error():
    msgbox.showerror("ERROR", "결제 오류")

def okcancel():
    msgbox.askokcancel("CONFIRM / CANCEL", "해당 좌석은 유아동반석입니다. 에매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("RETRY / CANCEL", "일시적인 오류가 발생하였습니다. 다시 시도하시겠습니까?")

    if response == 1:   # 재시도
        print("재시도")
    elif response == 0: # 취소
        print("취소")

def yesno():
    msgbox.askyesno("YES / NO", "헤당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = "예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # 예 => 저장 후 종료
    # 아니오 => 저장하지 않고 종료
    # 취소 => 프로그램 종료 취소 (현재 화면에서 계속 작업)

    print("응답: ", response)     # True, False, None -> 예 1, 아니오 0 그 외

    if response == 1:   # 예
        print("예")
    elif response == 0: # 아니오
        print("아니오")
    else:
        print("취소")


Button(root, command = info, text = "NOTICE").pack()
Button(root, command = warn, text = "WARNING").pack()
Button(root, command = error, text = "ERROR").pack()

Button(root, command = okcancel, text = "CONFIRM / CANCEL").pack()
Button(root, command = retrycancel, text = "CANCEL RETRY").pack()
Button(root, command = yesno, text = "YES / NO").pack()
Button(root, command = yesnocancel, text = "YES / NO / CANCEL").pack()

root.mainloop()