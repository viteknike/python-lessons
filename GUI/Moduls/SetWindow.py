def setwindow(root, w, h):
    root.title('Окно программы')
    root.resizable(False, False)

    if w == 0:
        w = 800
    else:
        w = w
    if h == 0:
        h = 600
    else:
        h = h
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int((ws/2) - (w/2))
    y = int((wh/2) - (h/2))


    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))
