from tkinter import *

root = Tk()
root.title("STUDY GUI")

btn1 = Button(root, text = "button 1")
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10, text = "button 2")
btn2.pack()

root.mainloop()