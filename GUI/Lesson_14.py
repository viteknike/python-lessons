from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

photo = PhotoImage(file='python-logo.png')
bgimage = photo.zoom(2, 2)

bg = Label(root, image=photo)

buttonimage = photo.subsample(2, 2)
button = Button(root, image=buttonimage)

bg.place(x=0, y=0, relwidth=1, relheight=1)
button.pack()

root.mainloop()