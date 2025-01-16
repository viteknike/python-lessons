from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

label = Label(root, text='Metka 1', font=('Tahoma', 20), bg='red')
label2 = Label(root, text='Metka 2', font=('Tahoma', 20), bg='green')
label3 = Label(root, text='Metka 3', font=('Tahoma', 20), bg='blue')
label4 = Label(root, text='Metka 4', font=('Tahoma', 20), bg='#9a3')
label5 = Label(root, text='Metka 5', font=('Tahoma', 20), bg='#777')

label.grid(column=0, row=0, padx=10, pady=20)
label2.grid(column=1, row=0, ipadx=10, ipady=20)
label3.grid(column=0, row=1, columnspan=2, pady=20, ipadx=40)
label4.grid(column=0, row=2, rowspan=2, sticky='e')
label5.grid(column=1, row=2, sticky='w')
Label(root, text='Metka 6', font=('Tahoma', 20), bg='#bdd').grid(row=3, column=1)

root.mainloop()