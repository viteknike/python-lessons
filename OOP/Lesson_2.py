class Point:
    x = 0
    y = 0
p1 = Point()
print(p1)
print(p1.x, p1.y)

p1.x = 5
p1.y = 7
print(p1.x, p1.y)

p2 = Point()
p2.z = 10
print(p2.x, ';', p2.z)

# print(p1.z) #Ошибка

print('------------------DZ-----------------------------')

class Rectangle:
    lt = 0
    weight = 5
    height = 10

p2 = Rectangle()
p2.lt = 12
p2.weight = 10
p2.height = 20
print(p2.lt, p2.weight, p2.height)

