from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

text = Text(root, width=10, height=10)

handler = open('text.txt', 'r')
x = handler.read()
handler.close()

text.insert(END, x)


text.pack()
root.mainloop()