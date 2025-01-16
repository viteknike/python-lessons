from datetime import *
from time import *

start = time()

print(date.today())
print(datetime.today())

d = date(2025, 7, 15)
print(d)

dt = datetime(2025, 7, 15, 12, 50, 30)
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print('-------------------')

print(dt.strftime('%Y.%m.%d %H:%M:%S'))
print(dt.strftime('%Y/%m/%d %H:%M.%S'))

print('-------------------')

print(time())

dt = datetime.fromtimestamp(393339399)
print(dt)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print(dt.timestamp())

i = 0
while i < 1000000:
    i += 1

print('time ago: ', time() - start, 'sec')

print('----------------------DZ-------------------------')

year = int(input('Введите год своего рождения: '))
month = int(input('Введите месяц своего рождения: '))
day = int(input('Введите день своего рождения: '))
dt = datetime(year, month, day)


second = time() - dt.timestamp()
minute = second // 60
hour = minute // 60
day = hour // 24


print(int(second), 'sec')
print(int(minute), 'minutes')
print(int(hour), 'hours')
print(int(day), 'days')