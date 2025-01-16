a = 0
while True:
    a += 0.1
    if a >= 1:
        exit(0)
    print('Hello')

#DZ

x = [15, 22, -7, -1, 7, -94]


def minus(list):
    newList = []
    for i in list:
        if i < 0:
            newList.append(i)
    return newList


print(minus(x))