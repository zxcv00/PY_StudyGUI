from tkinter import *

root = Tk()
root.title("STUDY GUI")
root.geometry("640x480")

label1 = Label(root, text = "HI")
label1.pack()

photo = PhotoImage(file = "GUI_BASIC/img.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "see you")

    global photo2
    photo2 = PhotoImage(file = "GUI_BASIC/img2.png")
    label2.config(image = photo2)

btn = Button(root, text = "click", command = change)
btn.pack()

root.mainloop()