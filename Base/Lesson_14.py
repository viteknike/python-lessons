def printpython():
    print('Python')

def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def summaprint(x, y, r = False):
    s = sum(x, y)
    if r:
        return s
    else:
        print(s)

def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

def printdict(**dict):
    for key in dict:
        print(key, '=', dict[key])

printpython()

s = sum(5, 7)
print(s)
print(sub(10, 15))

summaprint(15, 7)
print(summaprint(15, 7, True))

print(sub(y = 10, x = 5))

print(bigsum(10, 15, 3, 29, 6, 12))

printdict(name = 'alex', age = 30)

print('''
Анонимные функции
    ''')
lambdafunc = lambda x,y: print(x + y)
lambdafunc(5,7)

result = (lambda x, y: x + y) (1, 3)
print(result)

#DZ

def chet(x):
    n = x%2
    if n == 0:
        return True
    else:
        return False
print(chet(143))

def check(*num):
    maxNum = 0
    for n in num:
        if n > maxNum:
            maxNum = n
    print(maxNum)
    return maxNum
check(10, 153, 3, 29, 6, 12)

def sredArifmet(*num):
    suma = 0
    for n in num:
        suma += n
    sredSum = suma / len(num)
    return sredSum

print(sredArifmet(10, 15, 3, 29, 6, 12))

