from tkinter import *
from Moduls.SetWindow import setwindow
from random import *

def handlerenter(e):
    root.configure(background=color[randint(0, 2)])
def handlerleave(e):
    root.configure(background='white')

root = Tk()
setwindow(root, 0, 0)

color = ['red', 'green', 'blue']

root.bind('<Enter>', handlerenter)
root.bind('<Leave>', handlerleave)

root.mainloop()