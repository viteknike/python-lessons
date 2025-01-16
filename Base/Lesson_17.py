try:
    a = float('abc')
except ValueError:
    print('Невозможность привести к числу!')

while True:
    a = input('Введите положительное число: ')
    try:
        a = float(a)
        if a <= 0:
            raise Exception('Число не положительное!')
    except ValueError:
        print('Невозможность привести к числу!')
    except Exception as exp:
        print(exp)
    else:
        print('Спасибо за корректный ввод!')
    finally:
        print('В любом случае, завершаем программу')
        break

#DZ

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

try:
    x = a/b
except ZeroDivisionError:
    print('Бесконечность')
    exit(0)
else:
    print(x)


