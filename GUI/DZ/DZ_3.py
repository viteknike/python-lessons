from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

button = Button(root, justify='left', text='''Click Me
                              Click Me
                              Click Me''',font='Times 20', bg='#02f', activebackground='#f0000f')
button2 = Button(root, justify='center', text='''Click Me
                              Click Me
                              Click Me''', font='Roboto 16', bg='#0d6f6c', activebackground='#fdd')
button3 = Button(root, justify='right', text='''Click Me
                              Click Me
                              Click Me''', font='Sans 20', bg='#cdcf66', activebackground='#fcc')

button.pack()
button2.pack()
button3.pack()
root.mainloop()