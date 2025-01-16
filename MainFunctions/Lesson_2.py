from logging import fatal

s1 = 'str_1'
s2 = 'str_2'

print(len(s1))
print(s1[1])
print(s1[-1])
print(s1[-2])
print(s1[1:3])

s1 = 'abc\nxyz'
s2 = r'abc\nxyz'
print(s1)
print(s2)

print('--------------')

s1 = 'hello'
s2 = s1 * 3
print(s1 * 2)
print(s2)

print(s1.find('l'))
print(s1.find('l', 3))

print('hah'.isdigit())
print(s1.isalpha())
print(s1.upper())
print(s1.lower())

print('-------')

print(ord('a'))
print(chr(65))

s1 = '             hello             '
print(s1)
print(s1.strip())

s1 = 'Здравствуйте, {0}. Вам {1} лет!'
print(s1.format('Alex', 30))
s1 = 'Здравствуйте, {name}. Вам {age} лет!'
print(s1.format(name = 'Alex', age = 30))

data = ('Alex', 30)
s1 = 'Здравствуйте, {0[0]}. Вам {0[1]} лет!'
print(s1.format(data))

s1 = 'int: {0:d} ; bin: {0:b}'
print(s1.format(5))

s1 = 'Round (150 / 47) : {0:.3}'
print(s1.format(150/47))

print('-------------DZ----------------')

#DZ

text = input('Введите что-нибудь:')

for i in text:
    print(i)



def isfloat(x):
    try:
        x = float(x)
        return True
    except ValueError:
        return False


i = True
while i:
    num = input('Введите только цифры: ')
    if isfloat(num):
        print('Спасибо!')
        i = False
    else:
        print('Некорректный ввод!')

while True:
    num = input('Введите только цифры: ')
    if num.isdigit():
        print('Спасибо!')
        break
    else:
        print('Некорректный ввод!')






