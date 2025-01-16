from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

data = ['Apple', 'Orange', 'Lemon']
list = Listbox(root, font='Tahoma 20', width=20, height=10, selectmode=MULTIPLE)

for d in data:
    list.insert(END, d)

list.selection_set(1, 1)

list.pack()
root.mainloop()