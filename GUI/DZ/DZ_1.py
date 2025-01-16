from tkinter import *

root = Tk()

root.title('Что-нибудь!')
root.resizable(False, False)

w = 1000
h = 500

ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()



x = int(ws - w)
y = int(ws * 0)

root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))

root.mainloop()