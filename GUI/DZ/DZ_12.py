from shutil import which
from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

loginLabel = Label(root, text="Login: ")
passwordLabel = Label(root, text="Password: ")

loginText = Entry(root, bg='grey')
passwordText = Entry(root, bg='grey', show="*")

enter = Button(root, bg='green', text='Enter')

loginLabel.place(relx=0, rely=0)
passwordLabel.place(relx=0, rely=0.1)
loginText.place(relx=0.1, rely=0)
passwordText.place(relx=0.1, rely=0.1)
enter.place(relx=0, rely=0.2, width=205, height=30)


root.mainloop()