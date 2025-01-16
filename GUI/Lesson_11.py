from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

label = Label(text='Metka 1', font='Tahoma 20', bg='blue')
label2 = Label(text='Metka 2', font='Tahoma 20', bg='red')
label3 = Label(text='Metka 3', font='Tahoma 20', bg='green')
label4 = Label(text='Metka 4', font='Tahoma 20', bg='gray')
label5 = Label(text='Metka 5', font='Tahoma 20', bg='brown')


label.pack(side='top', fill=X, expand=True, anchor='n')
label2.pack(side='right')
label3.pack(side='bottom')
label4.pack(side='left')
label5.pack()

root.mainloop()