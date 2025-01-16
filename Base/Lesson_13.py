mydict = dict()
print(mydict)
mydict = {'Name' : 'John', 'age' : 35}
print(mydict)

mydict = dict(Name = 'John', Age = 35, isMale = True)
print(mydict)

print(mydict['Age'])

print('--------------')

for key in mydict:
    print(key, '=', mydict[key])

multiple = ('Name', 'Age', 'isMale')
for key in multiple:
    print(key, '=', mydict[key])

print('--------------')

mydict = {i * 2 : i for i in range(1, 11)}
print(mydict)
mydict = {str(i * 2) : i for i in range(1, 11)}
print(mydict)

print('--------------')

#DZ

user = dict(Name = 'Без имени', Age = -1)

userName = input('Введите свое имя : ')
userAge = input('Введите свой возраст : ')

user['Name'] = userName
user['Age'] = userAge

for key in user:
    print(key, '=', user[key])
