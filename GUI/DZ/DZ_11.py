from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

label = Label(root, text="Hello World", width=20, height=5)
label2 = Label(root, text="Hello World", width=20, height=5)
label3 = Label(root, text="Hello World", width=20, height=5)
label4 = Label(root, text="Hello World", width=20, height=5)

label.pack(side=TOP)
label2.pack(side=LEFT)
label3.pack(side=RIGHT)
label4.pack(side=BOTTOM)

root.mainloop()