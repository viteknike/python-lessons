from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

frame = Frame(root, bg='black', bd=10)
frame2 = Frame(root, bg='blue', bd=1)
frame3 = Frame(root, bg='green', bd=1)

label = Label(frame, text='Важная форма')

entry = Entry(frame2, font='Tahoma 20', bd=2)
entry2 = Entry(frame2, font='Tahoma 20', bd=2)

button = Button(frame3, font='Tahoma 20', text='Отправить форму')

frame.pack()
frame2.pack()
frame3.pack()
label.pack()
entry.pack()
entry2.pack()
button.pack()

root.mainloop()