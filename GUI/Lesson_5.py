from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

text = Text(root, bd=2, font='Tahoma 20', bg='Yellow', fg='Green', width=10, height=4)
text.insert(END, 'dick')
print(text.get(1.0, END))



text.pack()
root.mainloop()