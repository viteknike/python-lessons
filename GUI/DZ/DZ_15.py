from tkinter import *
from Moduls.SetWindow import setwindow
from random import *

def randnum(e):
    label.config(text=randint(1, 100))

root = Tk()
setwindow(root, 0, 0)

button = Button(root, font='Tahoma 20',text="Сгенерировать случайное число")



button.bind("<Button-1>", randnum)

text = StringVar()
label = Label(root, text=0)


button.pack()
label.pack()

root.mainloop()