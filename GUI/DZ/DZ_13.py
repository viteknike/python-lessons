from shutil import which
from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

labelAuth = Label(root, text='Авторизация', font=('Tahoma', 40))
labelLogin = Label(root, text='Login:', font=('Tahoma', 20))
inputLogin = Entry(root, font=('Tahoma', 20), bg='#686868')
labelPassword = Label(root, text='Password:', font=('Tahoma', 20))
inputPassword = Entry(root, font=('Tahoma', 20), bg='#686868', show='*')
buttonLogin = Button(root, text='Log in', font=('Tahoma', 20), bg='green')

labelAuth.grid(row=0, column=0, columnspan=2)
labelLogin.grid(column=0, row=1, sticky=W, ipadx=20)
inputLogin.grid(column=1, row=1)
labelPassword.grid(column=0, row=2, sticky=W, ipadx=20)
inputPassword.grid(column=1, row=2)
buttonLogin.grid(column=0, row=3, columnspan=2, pady=20, ipadx=60)

root.mainloop()