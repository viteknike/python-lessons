import os


handler = open('a.txt', 'w')
handler.write('Hello World\n890')
handler.close()

handler = open('a.txt', 'r')
print(handler.read(2))
print(handler.read())

handler.seek(0)
print(handler.read())

handler.seek(0)

for line in handler:
    print(line)

handler.close()

print('----------------------')

file = 'b.txt'

while True:
    print('1 - Записать файл;\n2 - Прочитать файл;\n0 - Выход')
    inp = input('Введите команду: ')
    if inp == '0':
        break
    elif inp == '1':
        text = input('Введите строку: ')
        handler = open(file, 'w')
        handler.write(text)
        handler.close()
    elif inp == '2':
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print('Файл еще не создан')
    else:
        print('Неизвестная команда')

print('''
-----------------DZ-------------------
''')


while True:
    print('1 - Прочитать файл;\n2 - Скопировать файл;\n0 - Выход')
    inp = input('Введите команду: ')
    if inp == '0':
        exit(0)
    elif inp == '1':
        x = input('Напишите путь к файлу, содержимое которого Вы хотите посмотреть: ')
        handler = open(x, 'r')
        print(handler.read())
        handler.close()
    elif inp == '2':
        x = input('Напишите путь к файлу, который Вы хотите скопировать: ')
        handler = open(x, 'r')
        name = os.path.basename(handler.name)
        text = handler.read()
        handler.close()
        handler = open(f'files/{name}', 'w')
        handler.write(text)
        handler.close()