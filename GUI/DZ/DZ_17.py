from tkinter import *
from Moduls.SetWindow import setwindow

def reskorn(e=False):
    global a
    global b
    global c
    print(a, b, c)
    try:
        print(int(b.get()))
        d = ((int(b.get())**2)-(4*int(a.get())*int(c.get())))

        print(d.real)
        if d.real > 0:
            d = d**0.5
            resx = (-int(b.get()) + round(d.real, 3))/(2*int(a.get()))
            resx2 = (-int(b.get()) - round(d.real, 3))/(2*int(a.get()))
            resultlabel.config(text='x1: '+str(round(resx.real, 4))+', x2: '+str(round(resx2.real, 4)))
        elif d.real == 0:
            resx = -int(b.get())/(2*int(a.get()))
            resultlabel.config(text='x: ' + str(round(resx.real, 4)), bg='#f0f0f0')
        else:
            resultlabel.config(text='Корней нет', bg='#f0f0f0')
    except ValueError:
        if not a.get() or not b.get() or not c.get():
            resultlabel.config(text='Введите значения', bg='red')
        else:
            resultlabel.config(text='Введите число', bg='red')


root = Tk()
setwindow(root, 400, 450)


label = Label(root, text='ax^2 + bx + c = 0', font='Tahoma 22', borderwidth=1, relief="solid")
labela = Label(root, text='a:', font='Tahoma 20')
labelb = Label(root, text='b:', font='Tahoma 20')
labelc = Label(root, text='c:', font='Tahoma 20')
a = Entry(root, font='Tahoma 20')
b = Entry(root, font='Tahoma 20')
c = Entry(root, font='Tahoma 20')
button = Button(root, text='Вычислить корни уравнения', font='Tahoma 20', bg='white', command=reskorn)
resultlabel = Label(root, text='', font='Tahoma 20')

root.bind('<Return>', reskorn)

label.grid(column=0, row=0, columnspan=2,pady=10, ipady=10, ipadx=15)
labela.grid(column=0, row=1, pady=10)
labelb.grid(column=0, row=2, pady=10)
labelc.grid(column=0, row=3, pady=10)
a.grid(column=1, row=1)
b.grid(column=1, row=2)
c.grid(column=1, row=3)
button.grid(column=0, row=4, pady=20, padx=10, columnspan=2)
resultlabel.grid(column=0, row=5, columnspan=2, ipady=10, ipadx=15)

root.mainloop()