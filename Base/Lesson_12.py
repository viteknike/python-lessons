mytuple = tuple()
print(mytuple)
mytuple = ()
print(mytuple)

#создание кортежа из одного элемента
mytuple = (1,)
print(mytuple)

mytuple = (1, '3', '5')
print(mytuple)
#mytuple[1] = '5' #ошибка
print(mytuple[1])

mytuple = tuple('Python')
print(mytuple)

#DZ


x = input('Введите что-нибудь :')

mytuple = tuple(x)

for i in mytuple:
    print(i)