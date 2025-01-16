from random import random
from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 800, 600)

label = Label(root, text='Моя метка', font='Tahoma 18', bg='#f0c', fg='#cc0000')



label.pack()

root.mainloop()



