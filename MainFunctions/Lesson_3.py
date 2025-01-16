list = [1, 2, 0, 5]
print(list)
list.append(9)
print(list)
list.extend([0, 1])
print(list)
list.insert(1, 5)
print(list)

print('-------------')

print(list.index(0))
print(list.index(0,4))
#print(list.index('a'))
print(list.count(0))

print('---------------')

list.reverse()
print(list)

print('--------------')

list.remove(0)
print(list)
list.pop(3)
print(list)
list.clear()
print(list)

print('----------------')

list = [1, 3, 0, 5, 1]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#Все операции работают с кортежами, кроме тех что меняют содержимое

t = tuple('Hello')
print(t.index('e'))
print(t.count('l'))

print('------------DZ------------------')
#DZ

x = input('Введите желаемое количество эл-тов в списке: ')
list = []
i = 0
while i <= int(x) - 1:
    n = input(f'Введите число {i + 1}: ')
    list.append(n)
    i += 1
print(list)
