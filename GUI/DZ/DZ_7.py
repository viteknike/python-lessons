from random import randint
from tkinter import *
from Moduls.SetWindow import setwindow
import os

root = Tk()
setwindow(root, 0, 0)

list = ('Сочи', 'Краснодар', 'Москва', 'Питер', 'Новосибирск')
label = Label(root, text='Выберите ваш любимый город: ')

label.pack()

choise = IntVar()
for i in range(0, len(list)):
    r = Radiobutton(root, text=list[i], variable=choise, value=i)
    r.pack()
choise.set(0)

root.mainloop()