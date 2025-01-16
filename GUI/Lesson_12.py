from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

label = Label(text='Metka 1', font='Tahoma 20', bg='blue')
label2 = Label(text='Metka 2', font='Tahoma 20', bg='red')
label3 = Label(text='Metka 3', font='Tahoma 20', bg='green')
label4 = Label(text='Metka 4', font='Tahoma 20', bg='gray')
label5 = Label(text='Metka 5', font='Tahoma 20', bg='brown')


label.place(x=10, y=20)
label2.place(relx=0.5, rely=0.5, anchor=CENTER)
label3.place(relx=0.5, rely=0, anchor=N)
label4.place(relx=0.5, rely=0.7, width=70, height=100, anchor=CENTER)
label5.place(relx=1, y=0, anchor=NE)

root.mainloop()