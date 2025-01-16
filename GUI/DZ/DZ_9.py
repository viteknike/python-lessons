from random import randint
from tkinter import *
from Moduls.SetWindow import setwindow
import os

root = Tk()
setwindow(root, 0, 0)

city = []
list = Listbox(root, font='Tahoma 20', width=20, height=10, selectmode=MULTIPLE)

while True:
    text = input('Введите город: ')
    if text == '0':
        break
    else:
        city.append(text)

for city in city:
    list.insert(END, city)


list.pack()
root.mainloop()