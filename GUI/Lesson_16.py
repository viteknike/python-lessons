from tkinter import *
from Moduls.SetWindow import setwindow

def handlerenter(e):
    e.widget.config(bg='red')
def handlerleave(e):
    e.widget.config(bg='yellow')

root = Tk()
setwindow(root, 0, 0)

button = Button(root, text="Кнопка 1", font='Tahoma 20', bg='yellow')
button2 = Button(root, text="Кнопка 2", font='Tahoma 20', bg='green')

button.bind('<Enter>', handlerenter)
button2.bind('<Enter>', handlerenter)
button.bind('<Leave>', handlerleave)
button2.bind('<Leave>', handlerleave)

button.pack()
button2.pack()

root.mainloop()