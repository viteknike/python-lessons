from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 800, 600)

button = Button(root, text="Click Me", bg='#fcd', fg='purple', font='Tahoma 18')
button2 = Button(root, text="Click Me", bg='#fcd', fg='purple', font='Tahoma 22')
print(button)

button.pack()
button2.pack()
root.mainloop()



