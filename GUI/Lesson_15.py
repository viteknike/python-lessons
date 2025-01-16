from tkinter import *

from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

def handlerclick(args):
    print('Нажата кнопка', str(args))
def handlerclick2():
    print('нажата кнопка 2')
def handlerclick3(event):
    print(event.widget)
    print('кликнули правой кнопкой мыши по кнопке: ')
    print(event.widget.cget('text'))
def handlerroot(event):
    print(event)
    print('Сработало событие')

button = Button(root, text='knopka 1', font='Tahoma 20', command=lambda: handlerclick('knopka 1'))
button2 = Button(root, text='knopka 2', font='Tahoma 20', command=handlerclick2)
button3 = Button(root, text='knopka 3', font='Tahoma 20')

button.bind('<Button-3>', handlerclick3)
button2.bind('<Button-3>', handlerclick3)
button3.bind('<Button-3>', handlerclick3)
root.bind('a', handlerroot)
root.bind('<Control-c>', handlerroot)

button.pack()
button2.pack()
button3.pack()

root.mainloop()