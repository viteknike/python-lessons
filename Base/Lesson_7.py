print('Введите свой возраст:')
a = input()

if int(a) >= 18:
    print('Вход разрешен')
elif int(a) <= 17:
    print('Пошел на хуй!')

cond = a == '0' or a == '1' or a == '2'
x = input()
cond = x if cond else 3
print(cond)

if cond:
    x = 0
else:
    x = 3

#DZ

x = input('Введите первое число: ')
y = input('Введите второе число: ')

if y == '0':
    print('Бесконечность')
else:
    print(x,'/',y,'=',int(x)/int(y))

