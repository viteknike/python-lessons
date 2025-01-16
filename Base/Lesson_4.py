x = 5
y = 7

text = 'равно'

#Основные математические операции

print('x + y', text, x + y)
print('x - y', text, x - y)
print('x * y', text, x * y)
print('x / y', text, x / y)
print('x % y', text, x % y)
print('x // y', text, x // y)
print('x ** y', text, x ** y)

#Битовые операции

x = 57
print('x =', x, bin(x))#Двоичная
print('x =', x, hex(x))#Шестнадцатиричная
print('x =', x, oct(x))#Восмиричная

print('-------------------------')

print('x | y', bin(x|y))
print('x & y', bin(x & y))
print('x ^ y', bin(x ^ y))
print('~x', bin(~x))
print('x << 1', x << 1)
print('x >> 1', x >> 1)

print('-------------------------')

#DZ

x = 32
y = 15

print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x%y)
print(x//y)
print(x**y)

print(((15 * 10 - 20) / 2) + 14 * 10 + (-45))

bin = bin(x)
print(bin)

