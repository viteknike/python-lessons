from random import randint
from tkinter import *
from Moduls.SetWindow import setwindow
import os

root = Tk()
setwindow(root, 0, 0)

choise = IntVar()
check = Checkbutton(root, text='Checker', variable=choise, onvalue=1, offvalue=0)

choise.set(randint(0,1))

check.pack()
root.mainloop()