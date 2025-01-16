from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

choice = IntVar()
check = Checkbutton(root, bd=20, text='ok', variable=choice, onvalue=1, offvalue=0)
# check.select()
# check.deselect()

print(choice.get())


check.pack()
root.mainloop()