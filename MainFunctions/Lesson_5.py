from random import *

d = {'name' : 'Alex', 'age' : 35}
print(d)
d.setdefault('isWorking', True)
print(d)
print(d.get('age'))
d.pop('name')
print(d)

keys = list(d.keys())
print(keys)
print(keys[0])

print('-------------------')

values = list(d.values())
print(values)
print(values[0])

print('-------------------')

d['age'] = 40
d['isMale'] = True
print(d)

d.clear()
print(d)

print('----------------DZ-------------------')
#DZ

# d = {'Hello' : 'Здравствуй', 'Bye' : 'Пока', 'Lesson' : 'Урок'}
#
# keys = list(d.keys())
# values = list(d.values())
# while True:
#     num = randint(1, len(d)-1)
#     print(values[num])
#     while True:
#         x = input('Введите на английском: ')
#         if x.lower() == 'show':
#             print(d)
#         elif x.lower() == 'quit':
#             exit(0)
#         elif keys[num].lower() == x.lower():
#             break
#         else:
#             print('Неправильный ответ')

d = {'man' : 'человек, мужчина', 'woman' : 'женщина', 'body' : 'тело', 'head' : 'голова', 'shoulder' : 'плечо', 'arm' : 'рука', 'hand' : 'рука(кисть)', 'elbow' : 'локоть', 'chest' : 'грудная клетка', 'stomach' : 'живот, желудок', 'back' : 'спина', 'bottom' : 'зад', 'thigh' : 'бедро', 'waist' : 'талия', 'leg' : 'нога', 'knee' : 'колено', 'foot' : 'ступня', 'ankle' : 'лодыжка', 'heel' : 'пятка', 'nail' : 'ноготь', 'shin' : 'голень', 'neck' : 'шея' , 'face' : 'лицо', 'nose' : 'нос', 'mouth' : 'рот', 'lip' : 'губа', 'tooth' : 'зуб', 'tongue' : 'язык', 'eye' : 'глаз', 'eyebrow' : 'бровь', 'eyelash' : 'ресница', 'pupil' : 'зрачок', 'eyelid' : 'веко', 'chin' : 'подбородок', 'cheek' : 'щека', 'forehead' : 'лоб', 'hair' : 'волосы', 'moustache' : 'усы', 'beard' : 'борода'}
ok = ['Вы молодец! -', 'Правильно! --', 'Так держать! ', 'Невероятно! -', 'Изумительно! ']
keys = list(d.keys())
while True:
    x = randint(0, len(d)-1)
    while True:
        translate = input(f'Переведите слово \'{d[keys[x]]}\' на английский язык: ')
        if translate.lower() == 'help':
            print(d)
        elif translate.lower() == 'exit':
            exit(0)
        elif keys[x].lower() == translate.lower():
            print(f'--------------------- {ok[randint(0, len(ok) - 1)]}---------------------')
            break
        else:
            print('--------------------- Вы ошиблись, повторите попытку... ---------------------')