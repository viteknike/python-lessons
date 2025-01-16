from tkinter import *
from random import randint
from Moduls.SetWindow import setwindow


root = Tk()
setwindow(root, 0, 0)

x = randint(1, 1000)
label = Label(root, text=x, font='Times 20 bold', bg='#0f0', fg='#f0c')

label.pack()
root.mainloop()