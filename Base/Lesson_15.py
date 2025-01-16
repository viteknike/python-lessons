from Base.Lesson_14 import result

isprint = True

def sum(x, y):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s

def sub(x, y):
    global result
    result = float(x) - float(y)

result = 0
isprint = False

x = input("Enter a number 1: ")
y = input("Enter a number 2: ")
print('sum =', sum(x,y))
sub(x, y)
print('result =', result)

#DZ

pi = 3.141592
def perim(radius):
    print(pi * radius * radius)
    return pi * radius * radius

print(perim(12))