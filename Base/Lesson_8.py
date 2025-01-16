i = 0
while i < 10:
    i += 1
    print('Hello world!')

print('----------------------')

i = 0
while i < 10:
    i += 1
    print(i)

print('----------------------')

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
print('while end, i =', i)

print('----------------------')

a = 0
x = 0
to = 10
while x <= to:
    a += x
    x += 1
print('Сумма чисел от 1 до', to, 'равна', a)

print('----------------------')

while True:
    code = input('Введите 0 для выхода: ')
    if code == '0':
        break
#exit(0)
print('----------------------')

#i = 0
#while True:
#    i += 1
#    print(i)

#DZ
x = 0
while True:
    y = input('Введите число для суммирования: ')
    if y == 'exit' or y == 'quit':
        print('Сумма всех чисел равна: ', x)
        break
    if y == 'sum':
        print('Сумма всех чисел равна: ', x)
        x = 0
        continue
    x += int(y)