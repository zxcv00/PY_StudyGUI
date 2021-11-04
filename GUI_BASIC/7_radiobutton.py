from tkinter import *

root = Tk()
root.title("STUDY GUI")
root.geometry("640x480")

label1 = Label(root, text = "> MENU <").pack()

burger_var = IntVar()        # 여기에 int 형으로 값을 저장
btn_burger1 = Radiobutton(root, text = "hambuger", value = 1, variable = burger_var)
btn_burger1.select()    # 기본값 선택
btn_burger2 = Radiobutton(root, text = "cheesebuger", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "chickenbuger", value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label1 = Label(root, text = "> BEVERAGE <").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "cola", value = "cola", variable = drink_var)
btn_drink1.select()     # 기본값 선택
btn_drink2 = Radiobutton(root, text = "sprite", value = "sprite", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
   print(burger_var.get())       # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
   print(drink_var.get())        # 음료 중 선택된 값을 출력

btn = Button(root, text = "order", command = btncmd)
btn.pack()

root.mainloop()