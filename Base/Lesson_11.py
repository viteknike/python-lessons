import random

myset = set()
print(myset)
myset = {}
print(myset)

myset = set('Python')
print(myset)

myset = {'1', 2, 3, 1, '1'}
print(myset)

print('''----------------------
''')

print(int(random.random() * 10))

print('''----------------------
''')

arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
myset = list(set(arr))
print(myset)

print('''----------------------
''')

#DZ

#1
x = int(input())

#2
arra = [int(random.random() * 100) for j in range(0, x)]

#3
print(arra)
y = 0
while y < len(arra):
    print(arra[y])
    y += 1

#4
myset = list(set(arra))
print(myset)
for x in myset:
    print(x)

print('''----------------------
''')
