array = [1, 5, 0, -5, 2.5]

for n in array:
    print(n)

print('''
----------------------
''')

str = 'python'
print(str[0])

for s in str:
    print(s)

print('''
----------------------
''')

x = 1
for s in str:
    if s == 'y':
        print('y находится под номером', x)
        break
    x += 1
else:
    print('Символа Y в строке', str, 'нет')

print('''
----------------------
''')

array = list(range(2, 15))
print(array[3])
for n in array:
    print(n)

print('''
----------------------
''')

array = [i * 2 for i in range(1, 11)]
print(array)
array = [i * 2 for i in range(1, 11)]
print(array)
array = [i for i in range(1, 11) if i % 2 == 0]
print(array)

print('''
----------------------
''')

#DZ

#1
array = [13, 25, 69, 43, 0]

#2
#x = sum(array)
x = 0
for n in array:
    x += n
print(x)

#3
x = 0
for n in array:
    x += n
print(x/len(array))




