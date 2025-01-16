from shutil import which
from tkinter import *
from Moduls.SetWindow import setwindow

root = Tk()
setwindow(root, 0, 0)

wayImage = input('Введите путь к картинке')

image = PhotoImage(file=wayImage)

zoomImage = input('Введите масштаб')

if zoomImage == '':
    imageEnd = image
elif float(zoomImage) > 0:
    imageEnd = image.zoom(int(zoomImage), int(zoomImage))
elif float(zoomImage) < 0:
    if abs(float(zoomImage)) < 1:
        imageEnd = image.subsample(int(1/abs(float(zoomImage))), int(1/abs(float(zoomImage))))
    elif abs(float(zoomImage)) > 1:
        imageEnd = image.subsample(int(zoomImage), int(zoomImage))

label = Label(root, image=imageEnd)
label.pack()

root.mainloop()