from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

entry = Entry(root, text='', font='Tahoma 20', bg='Yellow', fg='Green', bd=4)

input = input('Введите что-нибудь: ')
entry.insert(END, input)

entry.pack()
root.mainloop()