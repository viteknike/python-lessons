from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

entry = Entry(root, font='Tahoma 20', bg='Yellow', fg='Green', bd=4)
entry2 = Entry(root, font='Tahoma 20', bg='Yellow', fg='Green', bd=4, show='*')
entry.insert(END, 'Salam')
entry2.insert(END, '')

print(entry.cget('font'))
print(entry['font'])

entry.pack()
entry2.pack()

root.mainloop()