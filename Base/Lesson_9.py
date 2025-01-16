list = []
print(list)

list = ['h', 'e', 'l', 'l', 'o']
print(list)

print('Длина массива', len(list))
print('Последний элемент:', list[-1])
print('Последний элемент', list[len(list) - 1])

print('''
----------------------
''')

i = 0
while i < len(list):
    print(list[i])
    i += 1

print('''
----------------------
''')

list = [[1, 2], [3, 4, 5]]

i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j += 1
    i += 1

print('''
----------------------
''')

prices = [20, 30, 15, 20, 45, 15]
min = prices[0]
max = prices[0]
i = 0
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1
print('Max =', max, 'Min =', min)

#DZ

list = ['g', 'o', 'n', 'd', 'o', 'n']

i = 0
while i < len(list):
    print(i, '=', list[i])
    i += 1
x = input('Введите индекс необходимого объекта: ')
if int(x) <= len(list):
    print(list[int(x)])
elif int(x) > len(list):
    print('Элемента с таким индексом не существует')


