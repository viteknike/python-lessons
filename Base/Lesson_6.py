from unittest.mock import right

mystr1 = 'abc'
mystr2 = 'xyz'
print('конкатенация строк mystr1 и mystr2 =', mystr1 + mystr2)

mystr1 = '''Длинная строка 
на несколько 
строк'''

print(mystr1)

number1 = input('Введите первое число: ')
print('Вы ввели:', number1)
number2 = input('Введите второе число: ')
print('Вы ввели:', number2)
print('Сумма строк =', number1 + number2)

#print('Сумма строк =', int(number1) + int(number2))
print('Сумма строк =', float(number1) + float(number2))

#DZ

num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
num3 = input('Введите третье число: ')

print('Среднее арифметическое =', (int(num1) + int(num2) + int(num3))/3)


