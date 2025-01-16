from tkinter import *
from Moduls.SetWindow import setwindow

def handlerButton(e=False):
    global en1
    global en2
    global result
    if e:
        print(e)
    try:
        r = str(float(en1.get()) + float(en2.get()))
        result.config(text='Сумма чисел равна: ' + r)
    except ValueError:
        if not en1.get() and not en2.get():
            result.config(text='Вы не ввели числа')
        elif not en1.get():
            result.config(text='Вы не ввели первое число')
        elif not en2.get():
            result.config(text='Вы не ввели второе число')
        else:
            result.config(text='Вы ввели не числа')


root = Tk()
setwindow(root, 0, 0)

header = Label(root, text='Суммирование чисел', font='Tahoma 20')
en1 = Entry(root, font='Tahoma 20')
en2 = Entry(root, font='Tahoma 20')

button = Button(root, text='Сумма', font='Tahoma 20', command=handlerButton)
result = Label(root, font='Tahoma 20')

en1.bind('<Return>', handlerButton)
en2.bind('<Return>', handlerButton)

header.place(relx=0.5, rely=0.01, anchor='n')
en1.place(relx=0.5, rely=0.1, anchor='n')
en2.place(relx=0.5, rely=0.2, anchor='n')
button.place(relx=0.5, rely=0.3, anchor='n')
result.place(relx=0.5, rely=0.4, anchor='n')

root.mainloop()