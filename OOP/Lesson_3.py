class Circle:
    x = 0
    y = 0
    r = 0
    def __init__(self, x, y, r = 0):
        self.x = x
        self.y = y
        self.r = r
        if r == 0:
            print('Радиус не задан')

c = Circle(5, 7, 10)
print(c.x, ';', c.y, ';', c.r)
c.x = 10
print(c.x)

c = Circle(5, 20)
print(c.x, ';', c.y, ';', c.r)

print('-------------------DZ-----------------------')

class Rectangle:
    lt = 0
    w = 5
    h = 10
    def __init__(self, lt, w, h):
        self.lt = lt
        self.w = w
        self.h = h

r2 = Rectangle(5, 10, 20)
print(r2.lt, ';', r2.w, ';', r2.h)