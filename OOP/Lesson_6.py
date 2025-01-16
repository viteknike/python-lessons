class Shape:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print('(', self.x, '; ', self.y, ')', sep='')
    def draw(self):
        print('Рисуем фигуру')

class Circle(Shape):
    r = 0
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r
    def draw(self):
        print('Рисуем окружность (', self.x, '; ', self.y, '; ', self.r, ')', sep='')
class Rectangle(Shape):
    w = 0
    h = 0
    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
    def draw(self):
        print('Рисуем прямоугольник (', self.x, '; ', self.y, '; ', self.w, '; ', self.h, ')', sep='')
s = Shape(5, 5)
s.draw()

c = Circle(5, 5, 5)
c.draw()

r = Rectangle(5, 5, 5, 5)
r.draw()

s.printXY()

print('-----------------------DZ-----------------------')

class Auto:
    x = 0
    y =0
    motor = True
    circle = 4
    def move(self, x, y):
        print(f'Движение автомобиля в точку {x}, {y}')
        self.x = x
        self.y = y

class Tesla(Auto):
    motor = False
    def move(self, x, y):
        print(f'Движение автомобиля Tesla в точку {x}, {y}')
        self.x = x
        self.y = y

a = Auto()
print(a.x, a.y)
a.move(5, 5)
print(a.x, a.y)

t = Tesla()
t.move(12, 12)
print(t.x, t.y)


