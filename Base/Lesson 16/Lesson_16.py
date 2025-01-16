#import random
#import math as m
from random import *
from math import sin, cos
import math, cmath as cm
import calc
from dz import *



#print(random.random(0, 10))
#print(m.sin(1))
print(randint(0, 10))
print(sin(1))
print(cos(1))

print(math.ceil(10.3))
print(cm.log10(1000))

while True:
    r = 0
    print('1 - Сложение; 2 - Вычитание; 3 - Умножение; 4 - Деление; 0 - Выход')
    code = input('Введите команду: ')
    if code == '0':
        break
        #exit(0)
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    if code == '1':
        r = calc.add(a, b)
    if code == '2':
        r = calc.sub(a, b)
    if code == '3':
        r = calc.mult(a, b)
    if code == '4':
        r = calc.div(a, b)
    print('Результат:', r)

#DZ

print(maxnum(2,12,4,5,62))
print(minnum(2,12,4,5,62))
print(sumnum(2,12,4,5,62))

