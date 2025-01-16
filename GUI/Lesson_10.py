from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

frame = Frame(root, bg='red', bd=1)
frame2 = Frame(root, bg='blue', bd=10)

label = Label(frame, text='Metka 1', font='Tahoma 20')
label2 = Label(frame2, text='Metka 2', font='Tahoma 20')
label3 = Label(frame2, text='Metka 3', font='Tahoma 20')

frame.pack()
frame2.pack()
label.pack()
label2.pack()
label3.pack()

root.mainloop()