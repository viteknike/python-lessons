from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

text = Text(root, bd=2, font='Tahoma 20', bg='Yellow', fg='Black', width=40)

scrollbar = Scrollbar(root, orient=VERTICAL, command=text.yview)

text['yscrollcommand'] = scrollbar.set

text.pack(side=LEFT, fill=Y)
scrollbar.pack(side=LEFT, fill=Y)

root.mainloop()