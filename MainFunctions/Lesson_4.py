from random import *

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(len(set1))

set1.add(10)
print(set1)

#set1.remove(10)
set1.discard(10)
print(set1)

print('---------------')

#set1.issubset(set2)
#set1.issuperset(set2)
print(set1 == set2)
print(set1 <= set2)
print(set1 >= set2)

print('---------------')

set = {2, 3, 4}
set2 = {1, 2, 3}
print(set.union(set2))
print(set.intersection(set2))
print(set.difference(set2))

set1.clear()
set2.clear()
print(set1)
print(set2)

print('------------DZ-------------')
#DZ

set1 = {randint(1, 10) for i in range(10)}
set2 = {randint(1, 10) for i in range(10)}

print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
