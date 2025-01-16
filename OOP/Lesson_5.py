class Point:
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def __test(self):
        print('Private method')
    def runPrivate(self):
        self.__test()


p = Point(1, 2)
# print(p.__x) #ERROR
print(p.getX())
print(p.getY())
p.setX(3)
p.setY(4)
print(p.getX())
print(p.getY())

#p.__test() #ERROR

p.runPrivate()

print('-----------------DZ--------------------')

class Rectangle:
    __x = 0
    __y = 0
    __w = 5
    __h = 10
    def __printlog(self, met, x):
        if met == 'set':
            print('Изменено свойство:', x)
        else:
            print('Запрошено свойство:', x)
    def getX(self):
        self.__printlog('get', 'X')
        return self.__x
    def getY(self):
        self.__printlog('get', 'Y')
        return self.__y
    def getW(self):
        self.__printlog('get', 'W')
        return self.__w
    def getH(self):
        self.__printlog('get', 'H')
        return self.__h

    def setX(self, x):
        self.__printlog('set', 'X')
        self.__x = x
    def setY(self, y):
        self.__printlog('set', 'Y')
        self.__y = y
    def setW(self, w):
        self.__printlog('set', 'W')
        self.__w = w
    def setH(self, h):
        self.__printlog('set', 'H')
        self.__h = h
    def __str__(self):
        return f'Прямоугольник с координатами ({self.__x}; {self.__y}) шириной {self.__w} и высотой {self.__h}'
    def perimeter(self):
        return (self.__w + self.__h) * 2
    def area(self):
        return self.__w * self.__h

Rectangle().setW(5)
Rectangle().setX(8)
print(Rectangle().getW())
print(Rectangle().getH())